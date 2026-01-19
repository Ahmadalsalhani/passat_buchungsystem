from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from datetime import datetime, timedelta
import calendar
from .models import Booking
from .forms import BookingForm
from customers.models import Customer
from rooms.models import Room

@login_required
def dashboard(request):
    """Dashboard mit Statistiken"""
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='ausstehend').count()
    confirmed_bookings = Booking.objects.filter(status='bestaetigt').count()
    total_customers = Customer.objects.count()
    
    recent_bookings = Booking.objects.all()[:5]
    
    context = {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'total_customers': total_customers,
        'recent_bookings': recent_bookings,
    }
    return render(request, 'bookings/dashboard.html', context)

@login_required
def booking_list(request):
    """Liste aller Buchungen"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    bookings = Booking.objects.select_related('kunde', 'raum').all()
    
    if search_query:
        bookings = bookings.filter(
            Q(kunde__vorname__icontains=search_query) |
            Q(kunde__nachname__icontains=search_query) |
            Q(raum__raumnummer__icontains=search_query) |
            Q(raum__raumname__icontains=search_query)
        )
    
    if status_filter:
        bookings = bookings.filter(status=status_filter)
    
    context = {
        'bookings': bookings,
        'search_query': search_query,
        'status_filter': status_filter,
        'status_choices': Booking.STATUS_CHOICES,
    }
    return render(request, 'bookings/booking_list.html', context)

@login_required
def booking_detail(request, pk):
    """Detailansicht einer Buchung"""
    booking = get_object_or_404(Booking.objects.select_related('kunde', 'raum'), pk=pk)
    context = {'booking': booking}
    return render(request, 'bookings/booking_detail.html', context)

@login_required
def booking_create(request):
    """Neue Buchung anlegen"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save()
                messages.success(request, f'Buchung #{booking.pk} wurde erfolgreich erstellt.')
                return redirect('bookings:booking_detail', pk=booking.pk)
            except Exception as e:
                messages.error(request, f'Fehler beim Erstellen der Buchung: {str(e)}')
    else:
        form = BookingForm()
    
    context = {'form': form}
    return render(request, 'bookings/booking_form.html', context)

@login_required
def booking_update(request, pk):
    """Buchung bearbeiten"""
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                booking = form.save()
                messages.success(request, f'Buchung #{booking.pk} wurde erfolgreich aktualisiert.')
                return redirect('bookings:booking_detail', pk=booking.pk)
            except Exception as e:
                messages.error(request, f'Fehler beim Aktualisieren der Buchung: {str(e)}')
    else:
        form = BookingForm(instance=booking)
    
    context = {'form': form, 'booking': booking}
    return render(request, 'bookings/booking_form.html', context)

@login_required
def booking_delete(request, pk):
    """Buchung löschen"""
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        booking_id = booking.pk
        booking.delete()
        messages.success(request, f'Buchung #{booking_id} wurde erfolgreich gelöscht.')
        return redirect('bookings:booking_list')
    
    context = {'booking': booking}
    return render(request, 'bookings/booking_confirm_delete.html', context)

@login_required
def calendar_overview(request):
    """Kalenderübersicht mit allen Buchungen"""
    # Aktuelles Datum (heute) speichern
    today = datetime.now().date()
    
    # Jahr und Monat aus GET-Parameter oder Standard (heute)
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    
    # Ersten und letzten Tag des Monats bestimmen
    first_day = datetime(year, month, 1).date()
    if month == 12:
        last_day = datetime(year, 12, 31).date()
    else:
        last_day = (datetime(year, month + 1, 1) - timedelta(days=1)).date()
    
    # Alle Buchungen im ausgewählten Monat holen
    bookings = Booking.objects.filter(
        Q(check_in__lte=last_day) & Q(check_out__gte=first_day)
    ).select_related('kunde', 'raum').order_by('check_in')
    
    # Alle aktiven Räume
    rooms = Room.objects.filter(aktiv=True).order_by('raumnummer')
    
    # Kalenderstruktur erstellen
    cal = calendar.monthcalendar(year, month)
    
    # Farben für verschiedene Kunden
    customer_colors = {}
    color_palette = [
        '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
        '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B88B', '#AED6F1',
        '#FAD7A0', '#D7BDE2', '#A2D9CE', '#F5B7B1', '#D5F4E6'
    ]
    
    # Buchungsdaten für jede Tag und Raum organisieren
    calendar_data = {}
    for day in range(1, 32):
        try:
            day_date = datetime(year, month, day).date()
            calendar_data[day] = {}
            
            for room in rooms:
                # Alle Buchungen für diesen Tag und Raum finden
                day_bookings = bookings.filter(
                    raum=room,
                    check_in__lte=day_date,
                    check_out__gte=day_date
                )
                
                calendar_data[day][room.id] = []
                for booking in day_bookings:
                    # Farbe für Kunde zuweisen
                    if booking.kunde.id not in customer_colors:
                        color_idx = len(customer_colors) % len(color_palette)
                        customer_colors[booking.kunde.id] = color_palette[color_idx]
                    
                    calendar_data[day][room.id].append({
                        'booking': booking,
                        'color': customer_colors[booking.kunde.id],
                        'customer_name': booking.kunde.get_full_name()
                    })
        except ValueError:
            # Tag existiert nicht in diesem Monat
            pass
    
    # Vorheriger und nächster Monat
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
    
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    context = {
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'calendar': cal,
        'rooms': rooms,
        'calendar_data': calendar_data,
        'bookings': bookings,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'today_day': today.day,
        'today_month': today.month,
        'today_year': today.year,
        'is_current_month': today.year == year and today.month == month,
    }
    return render(request, 'bookings/calendar_overview.html', context)

@login_required
def customer_autocomplete(request):
    """AJAX Autocomplete für Kunden"""
    search_term = request.GET.get('q', '')
    
    if len(search_term) < 2:
        return JsonResponse({'results': []})
    
    customers = Customer.objects.filter(
        Q(vorname__icontains=search_term) |
        Q(nachname__icontains=search_term) |
        Q(id__icontains=search_term)
    )[:10]
    
    results = [{
        'id': customer.id,
        'text': f"{customer.get_full_name()} (#{customer.id})"
    } for customer in customers]
    
    return JsonResponse({'results': results})

@login_required
def room_autocomplete(request):
    """AJAX Autocomplete für Räume"""
    search_term = request.GET.get('q', '')
    
    if len(search_term) < 1:
        return JsonResponse({'results': []})
    
    rooms = Room.objects.filter(
        Q(raumnummer__icontains=search_term) |
        Q(raumname__icontains=search_term),
        aktiv=True
    )[:10]
    
    results = [{
        'id': room.id,
        'text': f"{room.raumnummer} - {room.raumname}"
    } for room in rooms]
    
    return JsonResponse({'results': results})
