from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'kunde', 'raum', 'check_in', 'check_out', 'anzahl_gaeste', 'status', 'gesamtpreis']
    list_filter = ['status', 'check_in', 'created_at']
    search_fields = ['kunde__vorname', 'kunde__nachname', 'raum__raumnummer', 'raum__raumname']
    readonly_fields = ['created_at', 'updated_at', 'anzahl_naechte', 'gesamtpreis']
    date_hierarchy = 'check_in'
    
    fieldsets = (
        ('Buchungsinformationen', {
            'fields': ('kunde', 'raum', 'check_in', 'check_out', 'anzahl_gaeste')
        }),
        ('Status und Notizen', {
            'fields': ('status', 'notizen')
        }),
        ('Berechnungen', {
            'fields': ('anzahl_naechte', 'gesamtpreis')
        }),
        ('Zeitstempel', {
            'fields': ('created_at', 'updated_at')
        }),
    )
