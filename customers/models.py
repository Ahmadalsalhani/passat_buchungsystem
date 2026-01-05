from django.db import models

class Customer(models.Model):
    """
    Kunden-Model mit vollständigen Kontaktdaten
    """
    ANREDE_CHOICES = (
        ('herr', 'Herr'),
        ('frau', 'Frau'),
        ('divers', 'Divers'),
    )
    
    anrede = models.CharField(max_length=10, choices=ANREDE_CHOICES, verbose_name='Anrede')
    vorname = models.CharField(max_length=100, verbose_name='Vorname')
    nachname = models.CharField(max_length=100, verbose_name='Nachname')
    email = models.EmailField(verbose_name='E-Mail')
    telefon = models.CharField(max_length=50, verbose_name='Telefon')
    
    # Adresse
    strasse = models.CharField(max_length=200, verbose_name='Straße')
    plz = models.CharField(max_length=10, verbose_name='PLZ')
    stadt = models.CharField(max_length=100, verbose_name='Stadt')
    land = models.CharField(max_length=100, default='Deutschland', verbose_name='Land')
    
    # Optional
    notizen = models.TextField(blank=True, verbose_name='Notizen')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Aktualisiert am')
    
    class Meta:
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'
        ordering = ['nachname', 'vorname']
    
    def __str__(self):
        return f"{self.get_anrede_display()} {self.vorname} {self.nachname}"
    
    def get_full_name(self):
        """Gibt den vollständigen Namen zurück"""
        return f"{self.vorname} {self.nachname}"
    
    def get_address(self):
        """Gibt die vollständige Adresse zurück"""
        return f"{self.strasse}, {self.plz} {self.stadt}, {self.land}"
