from django.db import models
from django.core.exceptions import ValidationError
from customers.models import Customer
from rooms.models import Room

class Booking(models.Model):
    """
    Buchungs-Model mit automatischen Berechnungen und Validierung
    """
    STATUS_CHOICES = (
        ('ausstehend', 'Ausstehend'),
        ('bestaetigt', 'Bestätigt'),
        ('storniert', 'Storniert'),
        ('abgeschlossen', 'Abgeschlossen'),
    )
    
    kunde = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Kunde', related_name='buchungen')
    raum = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name='Raum', related_name='buchungen')
    
    check_in = models.DateField(verbose_name='Check-in')
    check_out = models.DateField(verbose_name='Check-out')
    anzahl_gaeste = models.PositiveIntegerField(verbose_name='Anzahl Gäste')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ausstehend', verbose_name='Status')
    notizen = models.TextField(blank=True, verbose_name='Notizen')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Aktualisiert am')
    
    class Meta:
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'
        ordering = ['-check_in']
    
    def __str__(self):
        return f"Buchung #{self.pk} - {self.kunde.get_full_name()} - {self.raum.raumnummer}"
    
    def clean(self):
        """Validierung der Buchungsdaten"""
        if self.check_out and self.check_in:
            if self.check_out <= self.check_in:
                raise ValidationError('Check-out muss nach Check-in sein.')
        
        if self.anzahl_gaeste and self.raum:
            if self.anzahl_gaeste > self.raum.kapazitaet:
                raise ValidationError(f'Gästeanzahl darf Raumkapazität ({self.raum.kapazitaet}) nicht überschreiten.')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def anzahl_naechte(self):
        """Berechnet die Anzahl der Nächte"""
        if self.check_out and self.check_in:
            return (self.check_out - self.check_in).days
        return 0
    
    def gesamtpreis(self):
        """Berechnet den Gesamtpreis"""
        return self.anzahl_naechte() * self.raum.preis_pro_nacht
