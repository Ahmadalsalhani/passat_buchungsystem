from django.db import models
from bookings.models import Booking
from decimal import Decimal

class Invoice(models.Model):
    """
    Rechnungs-Model mit automatischer Berechnung
    """
    STATUS_CHOICES = (
        ('entwurf', 'Entwurf'),
        ('versendet', 'Versendet'),
        ('bezahlt', 'Bezahlt'),
        ('storniert', 'Storniert'),
    )
    
    buchung = models.OneToOneField(Booking, on_delete=models.PROTECT, verbose_name='Buchung', related_name='rechnung')
    rechnungsnummer = models.CharField(max_length=20, unique=True, verbose_name='Rechnungsnummer')
    rechnungsdatum = models.DateField(verbose_name='Rechnungsdatum')
    faelligkeitsdatum = models.DateField(verbose_name='Fälligkeitsdatum')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='entwurf', verbose_name='Status')
    
    mwst_satz = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('19.00'), verbose_name='MwSt.-Satz (%)')
    
    notizen = models.TextField(blank=True, verbose_name='Notizen')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Aktualisiert am')
    
    class Meta:
        verbose_name = 'Rechnung'
        verbose_name_plural = 'Rechnungen'
        ordering = ['-rechnungsdatum']
    
    def __str__(self):
        return f"Rechnung {self.rechnungsnummer} - {self.buchung.kunde.get_full_name()}"
    
    def zwischensumme(self):
        """Berechnet die Zwischensumme (ohne MwSt.)"""
        return self.buchung.gesamtpreis()
    
    def mwst_betrag(self):
        """Berechnet den MwSt.-Betrag"""
        return self.zwischensumme() * (self.mwst_satz / Decimal('100'))
    
    def gesamtbetrag(self):
        """Berechnet den Gesamtbetrag (inkl. MwSt.)"""
        return self.zwischensumme() + self.mwst_betrag()
    
    def save(self, *args, **kwargs):
        # Automatische Generierung der Rechnungsnummer wenn nicht vorhanden
        if not self.rechnungsnummer:
            last_invoice = Invoice.objects.all().order_by('id').last()
            if last_invoice:
                last_number = int(last_invoice.rechnungsnummer.split('-')[1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.rechnungsnummer = f'INV-{new_number:05d}'
        
        super().save(*args, **kwargs)
