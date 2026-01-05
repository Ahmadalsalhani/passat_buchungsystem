from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
from .models import Invoice
from .forms import InvoiceForm

@login_required
def invoice_list(request):
    """Liste aller Rechnungen"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    invoices = Invoice.objects.select_related('buchung__kunde', 'buchung__raum').all()
    
    if search_query:
        invoices = invoices.filter(
            Q(rechnungsnummer__icontains=search_query) |
            Q(buchung__kunde__vorname__icontains=search_query) |
            Q(buchung__kunde__nachname__icontains=search_query)
        )
    
    if status_filter:
        invoices = invoices.filter(status=status_filter)
    
    context = {
        'invoices': invoices,
        'search_query': search_query,
        'status_filter': status_filter,
        'status_choices': Invoice.STATUS_CHOICES,
    }
    return render(request, 'invoices/invoice_list.html', context)

@login_required
def invoice_detail(request, pk):
    """Detailansicht einer Rechnung"""
    invoice = get_object_or_404(Invoice.objects.select_related('buchung__kunde', 'buchung__raum'), pk=pk)
    context = {'invoice': invoice}
    return render(request, 'invoices/invoice_detail.html', context)

@login_required
def invoice_create(request):
    """Neue Rechnung anlegen"""
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            messages.success(request, f'Rechnung {invoice.rechnungsnummer} wurde erfolgreich erstellt.')
            return redirect('invoices:invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm()
    
    context = {'form': form}
    return render(request, 'invoices/invoice_form.html', context)

@login_required
def invoice_update(request, pk):
    """Rechnung bearbeiten"""
    invoice = get_object_or_404(Invoice, pk=pk)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save()
            messages.success(request, f'Rechnung {invoice.rechnungsnummer} wurde erfolgreich aktualisiert.')
            return redirect('invoices:invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
    
    context = {'form': form, 'invoice': invoice}
    return render(request, 'invoices/invoice_form.html', context)

@login_required
def invoice_delete(request, pk):
    """Rechnung löschen"""
    invoice = get_object_or_404(Invoice, pk=pk)
    
    if request.method == 'POST':
        number = invoice.rechnungsnummer
        invoice.delete()
        messages.success(request, f'Rechnung {number} wurde erfolgreich gelöscht.')
        return redirect('invoices:invoice_list')
    
    context = {'invoice': invoice}
    return render(request, 'invoices/invoice_confirm_delete.html', context)

@login_required
def invoice_pdf(request, pk):
    """PDF-Generierung für Rechnung"""
    invoice = get_object_or_404(Invoice.objects.select_related('buchung__kunde', 'buchung__raum'), pk=pk)
    
    # PDF erstellen
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Titel
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
    )
    elements.append(Paragraph('Rechnung', title_style))
    elements.append(Spacer(1, 0.5*cm))
    
    # Firmeninformationen
    company_info = [
        ['<b>Passat Buchungssystem</b>', ''],
        ['Musterstraße 123', f'<b>Rechnung Nr.:</b> {invoice.rechnungsnummer}'],
        ['12345 Musterstadt', f'<b>Datum:</b> {invoice.rechnungsdatum.strftime("%d.%m.%Y")}'],
        ['Deutschland', f'<b>Fällig am:</b> {invoice.faelligkeitsdatum.strftime("%d.%m.%Y")}'],
    ]
    
    company_table = Table(company_info, colWidths=[9*cm, 8*cm])
    company_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    elements.append(company_table)
    elements.append(Spacer(1, 1*cm))
    
    # Kundenadresse
    elements.append(Paragraph('<b>Rechnungsempfänger:</b>', styles['Heading3']))
    customer = invoice.buchung.kunde
    customer_info = f"""
    {customer.get_anrede_display()} {customer.vorname} {customer.nachname}<br/>
    {customer.strasse}<br/>
    {customer.plz} {customer.stadt}<br/>
    {customer.land}
    """
    elements.append(Paragraph(customer_info, styles['Normal']))
    elements.append(Spacer(1, 1*cm))
    
    # Buchungsdetails
    elements.append(Paragraph('<b>Buchungsdetails:</b>', styles['Heading3']))
    elements.append(Spacer(1, 0.3*cm))
    
    booking = invoice.buchung
    booking_data = [
        ['Beschreibung', 'Anzahl', 'Preis', 'Betrag'],
        [
            f'{booking.raum.raumname} ({booking.raum.get_raumtyp_display()})\n'
            f'Check-in: {booking.check_in.strftime("%d.%m.%Y")}\n'
            f'Check-out: {booking.check_out.strftime("%d.%m.%Y")}',
            f'{booking.anzahl_naechte()} Nächte',
            f'{booking.raum.preis_pro_nacht:.2f} €',
            f'{booking.gesamtpreis():.2f} €'
        ],
    ]
    
    booking_table = Table(booking_data, colWidths=[8*cm, 3*cm, 3*cm, 3*cm])
    booking_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(booking_table)
    elements.append(Spacer(1, 1*cm))
    
    # Zusammenfassung
    summary_data = [
        ['Zwischensumme:', f'{invoice.zwischensumme():.2f} €'],
        [f'MwSt. ({invoice.mwst_satz}%):', f'{invoice.mwst_betrag():.2f} €'],
        ['<b>Gesamtbetrag:</b>', f'<b>{invoice.gesamtbetrag():.2f} €</b>'],
    ]
    
    summary_table = Table(summary_data, colWidths=[14*cm, 3*cm])
    summary_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('LINEABOVE', (0, 2), (-1, 2), 2, colors.black),
        ('FONTNAME', (0, 2), (-1, 2), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 2), (-1, 2), 14),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 1*cm))
    
    # Notizen
    if invoice.notizen:
        elements.append(Paragraph('<b>Notizen:</b>', styles['Heading3']))
        elements.append(Paragraph(invoice.notizen, styles['Normal']))
        elements.append(Spacer(1, 0.5*cm))
    
    # Fußzeile
    footer_text = "Vielen Dank für Ihr Vertrauen!"
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph(footer_text, styles['Normal']))
    
    # PDF generieren
    doc.build(elements)
    
    # Response erstellen
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Rechnung_{invoice.rechnungsnummer}.pdf"'
    
    return response
