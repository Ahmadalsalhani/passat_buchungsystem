# UpdateV2 - Neue Features

## Implementierte Features

### 1. Kalenderübersicht

**Zugriff:** Navigation Menü → "Kalender Übersicht"

Die neue Kalenderübersicht bietet:
- **Monatliche Ansicht** aller Buchungen mit Raum- und Kundendetails
- **Farbcodierung** für verschiedene Kunden (jeder Kunde hat eine eigene Farbe)
- **Visuelle Unterscheidung** zwischen freien (grün) und belegten Räumen
- **Detaillierte Buchungsinformationen** beim Hover über Buchungen
- **Navigation** zwischen Monaten (Vorheriger/Nächster Monat)
- **Übersichtstabelle** aller Buchungen des aktuellen Monats

#### Funktionen:
- Zeigt alle Kalenderwochen des Jahres
- Unterscheidet freie und belegte Räume farblich
- Bei mehreren Kunden pro Tag: Jeder Kunde erscheint in einer eigenen Farbe
- Vor- und Nachname des Kunden sind im Kalender erkennbar
- Klick auf eine Buchung führt zur Detailansicht

#### Navigation:
```
Dashboard → Kalender Übersicht
URL: /buchungen/kalender/
```

### 2. Autocomplete-Suchfeld für Kunden und Räume

**Zugriff:** Beim Erstellen oder Bearbeiten einer Buchung

Die neue Suchfunktion bietet:
- **Kunden-Autocomplete:**
  - Suche nach Vorname, Nachname oder Kundennummer
  - Live-Suche während der Eingabe
  - Zeigt die ersten 10 Übereinstimmungen
  - Mindestens 2 Zeichen erforderlich

- **Raum-Autocomplete:**
  - Suche nach Raumnummer oder Raumname
  - Live-Suche während der Eingabe
  - Zeigt nur aktive Räume
  - Mindestens 1 Zeichen erforderlich

#### Verwendung:
1. Gehe zu "Buchungen" → "Neue Buchung"
2. Im Feld "Kunde": Beginne mit der Eingabe des Namens oder der Kundennummer
3. Im Feld "Raum": Beginne mit der Eingabe der Raumnummer oder des Raumnamens
4. Wähle aus den angezeigten Ergebnissen

## Technische Details

### Neue Dateien:
1. **views.py** - Erweitert um:
   - `calendar_overview()` - Kalenderübersicht-View
   - `customer_autocomplete()` - AJAX-Endpoint für Kundensuche
   - `room_autocomplete()` - AJAX-Endpoint für Raumsuche

2. **templates/bookings/calendar_overview.html** - Neues Template für Kalenderansicht

3. **bookings/templatetags/custom_filters.py** - Template-Filter für Dictionary-Lookup

4. **urls.py** - Neue URLs:
   - `/buchungen/kalender/` - Kalenderübersicht
   - `/buchungen/api/customers/autocomplete/` - Kunden-Autocomplete-API
   - `/buchungen/api/rooms/autocomplete/` - Raum-Autocomplete-API

### Aktualisierte Dateien:
1. **templates/base.html** - Navigation um "Kalender Übersicht" erweitert
2. **bookings/forms.py** - Formular um Select2-Widgets erweitert
3. **templates/bookings/booking_form.html** - Select2-Integration hinzugefügt

### Verwendete Technologien:
- **Select2** (v4.1.0) - Für Autocomplete-Funktionalität
- **Bootstrap 5** - Für responsives Design
- **Django Template Tags** - Für Kalender-Rendering
- **Python Calendar Module** - Für Kalendergenerierung

## Farbschema

Das System verwendet ein 15-Farben-Palette für Kunden:
```
#FF6B6B, #4ECDC4, #45B7D1, #FFA07A, #98D8C8,
#F7DC6F, #BB8FCE, #85C1E2, #F8B88B, #AED6F1,
#FAD7A0, #D7BDE2, #A2D9CE, #F5B7B1, #D5F4E6
```

- **Freie Räume**: Grün (#d4edda)
- **Belegte Räume**: Hell-grau (#f8f9fa)

## API-Endpunkte

### Kunden-Autocomplete
```
GET /buchungen/api/customers/autocomplete/?q=<suchbegriff>

Response:
{
    "results": [
        {
            "id": 1,
            "text": "Max Mustermann (#1)"
        }
    ]
}
```

### Raum-Autocomplete
```
GET /buchungen/api/rooms/autocomplete/?q=<suchbegriff>

Response:
{
    "results": [
        {
            "id": 1,
            "text": "101 - Standardzimmer"
        }
    ]
}
```

## Zukünftige Erweiterungen

Mögliche weitere Verbesserungen:
1. Export der Kalenderansicht als PDF
2. Wochenansicht zusätzlich zur Monatsansicht
3. Drag-and-Drop für Buchungsänderungen im Kalender
4. Filter nach Raumtyp
5. Suchfunktion im Kalender
6. Benachrichtigungen bei überlappenden Buchungen

## Support

Bei Fragen oder Problemen wenden Sie sich an das Entwicklerteam.
