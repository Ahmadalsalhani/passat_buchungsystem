from django.db import models

class Room(models.Model):
    """
    Raum-Model mit Eigenschaften und Preisen
    """
    ROOM_TYPE_CHOICES = (
        ('einzelzimmer', 'Einzelzimmer'),
        ('doppelzimmer', 'Doppelzimmer'),
        ('suite', 'Suite'),
        ('konferenzraum', 'Konferenzraum'),
    )
    
    raumnummer = models.CharField(max_length=20, unique=True, verbose_name='Raumnummer')
    raumname = models.CharField(max_length=100, verbose_name='Raumname')
    raumtyp = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, verbose_name='Raumtyp')
    kapazitaet = models.PositiveIntegerField(verbose_name='Kapazität')
    preis_pro_nacht = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preis pro Nacht')
    beschreibung = models.TextField(blank=True, verbose_name='Beschreibung')
    aktiv = models.BooleanField(default=True, verbose_name='Aktiv')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Aktualisiert am')
    
    class Meta:
        verbose_name = 'Raum'
        verbose_name_plural = 'Räume'
        ordering = ['raumnummer']
    
    def __str__(self):
        return f"{self.raumnummer} - {self.raumname} ({self.get_raumtyp_display()})"
