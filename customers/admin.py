from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['nachname', 'vorname', 'anrede', 'email', 'telefon', 'stadt', 'created_at']
    list_filter = ['anrede', 'land', 'created_at']
    search_fields = ['vorname', 'nachname', 'email', 'telefon', 'stadt']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Persönliche Daten', {
            'fields': ('anrede', 'vorname', 'nachname', 'email', 'telefon')
        }),
        ('Adresse', {
            'fields': ('strasse', 'plz', 'stadt', 'land')
        }),
        ('Zusätzliche Informationen', {
            'fields': ('notizen', 'created_at', 'updated_at')
        }),
    )
