from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['raumnummer', 'raumname', 'raumtyp', 'kapazitaet', 'preis_pro_nacht', 'aktiv']
    list_filter = ['raumtyp', 'aktiv', 'created_at']
    search_fields = ['raumnummer', 'raumname']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Rauminformationen', {
            'fields': ('raumnummer', 'raumname', 'raumtyp', 'kapazitaet')
        }),
        ('Preis und Status', {
            'fields': ('preis_pro_nacht', 'aktiv')
        }),
        ('Beschreibung', {
            'fields': ('beschreibung',)
        }),
        ('Zeitstempel', {
            'fields': ('created_at', 'updated_at')
        }),
    )
