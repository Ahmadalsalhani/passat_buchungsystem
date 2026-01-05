from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['rechnungsnummer', 'buchung', 'rechnungsdatum', 'faelligkeitsdatum', 'status', 'gesamtbetrag']
    list_filter = ['status', 'rechnungsdatum', 'created_at']
    search_fields = ['rechnungsnummer', 'buchung__kunde__vorname', 'buchung__kunde__nachname']
    readonly_fields = ['created_at', 'updated_at', 'zwischensumme', 'mwst_betrag', 'gesamtbetrag']
    date_hierarchy = 'rechnungsdatum'
    
    fieldsets = (
        ('Rechnungsinformationen', {
            'fields': ('buchung', 'rechnungsnummer', 'rechnungsdatum', 'faelligkeitsdatum')
        }),
        ('Status und MwSt.', {
            'fields': ('status', 'mwst_satz')
        }),
        ('Berechnungen', {
            'fields': ('zwischensumme', 'mwst_betrag', 'gesamtbetrag')
        }),
        ('Notizen', {
            'fields': ('notizen',)
        }),
        ('Zeitstempel', {
            'fields': ('created_at', 'updated_at')
        }),
    )
