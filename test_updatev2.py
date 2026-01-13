# Test Script für UpdateV2 Features
# Dieses Script kann verwendet werden, um die neuen Features zu testen

"""
MANUELLE TEST-CHECKLISTE

1. KALENDERÜBERSICHT TESTEN:
   ☐ Im Browser zur URL navigieren: http://localhost:8000/buchungen/kalender/
   ☐ Überprüfen, dass der aktuelle Monat angezeigt wird
   ☐ Navigation testen:
     - Klick auf "Vorheriger Monat"
     - Klick auf "Nächster Monat"
     - Klick auf "Heute"
   ☐ Überprüfen der Farbanzeige:
     - Freie Räume sollten grün sein
     - Belegte Räume sollten grau sein
   ☐ Buchungen überprüfen:
     - Sind Kundennamen sichtbar?
     - Haben verschiedene Kunden verschiedene Farben?
   ☐ Hover über Buchung - Tooltip sollte Details zeigen
   ☐ Klick auf Buchung - sollte zur Detailseite führen
   ☐ Tabelle unter Kalender überprüfen - zeigt alle Buchungen

2. AUTOCOMPLETE TESTEN:
   ☐ Neue Buchung erstellen: http://localhost:8000/buchungen/neu/
   ☐ Kunden-Autocomplete:
     - Feld "Kunde" anklicken
     - Mindestens 2 Buchstaben eines Kundennamens eingeben
     - Dropdown sollte erscheinen mit passenden Kunden
     - Kunde aus Liste auswählen
   ☐ Raum-Autocomplete:
     - Feld "Raum" anklicken
     - Mindestens 1 Buchstabe einer Raumnummer eingeben
     - Dropdown sollte erscheinen mit passenden Räumen
     - Raum aus Liste auswählen
   ☐ Formular absenden und überprüfen, dass Buchung erstellt wurde

3. NAVIGATION TESTEN:
   ☐ Im Menü sollte "Kalender Übersicht" zwischen "Dashboard" und "Kunden" sein
   ☐ Klick auf "Kalender Übersicht" führt zur Kalenderseite
   ☐ Button sollte aktiv (hervorgehoben) sein, wenn auf der Kalenderseite

4. RESPONSIVE DESIGN TESTEN:
   ☐ Kalender auf verschiedenen Bildschirmgrößen testen
   ☐ Horizontales Scrollen bei kleinen Bildschirmen überprüfen
   ☐ Mobile Ansicht überprüfen

5. FEHLERBEHANDLUNG TESTEN:
   ☐ Kalender bei leerem Monat (keine Buchungen) öffnen
   ☐ Autocomplete mit nicht existierenden Daten testen
   ☐ Sehr langen Kundennamen im Kalender überprüfen

BEKANNTE VORAUSSETZUNGEN:
- Django-Server muss laufen
- Datenbank muss Testdaten enthalten (Kunden, Räume, Buchungen)
- Bootstrap 5 und Select2 CDN müssen erreichbar sein
"""

# Python-Code zum Erstellen von Testdaten (falls benötigt)
# Diesen Code in der Django Shell ausführen: python manage.py shell

TEST_DATA_CREATION = """
from customers.models import Customer
from rooms.models import Room
from bookings.models import Booking
from datetime import date, timedelta

# Testkunden erstellen
kunde1 = Customer.objects.create(
    anrede='herr',
    vorname='Max',
    nachname='Mustermann',
    email='max@example.com',
    telefon='0123456789',
    strasse='Musterstraße 1',
    plz='12345',
    stadt='Musterstadt',
    land='Deutschland'
)

kunde2 = Customer.objects.create(
    anrede='frau',
    vorname='Anna',
    nachname='Schmidt',
    email='anna@example.com',
    telefon='0987654321',
    strasse='Testweg 5',
    plz='54321',
    stadt='Teststadt',
    land='Deutschland'
)

# Testräume erstellen
raum1 = Room.objects.create(
    raumnummer='101',
    raumname='Standardzimmer',
    raumtyp='einzelzimmer',
    kapazitaet=2,
    preis_pro_nacht=75.00,
    aktiv=True
)

raum2 = Room.objects.create(
    raumnummer='102',
    raumname='Komfortzimmer',
    raumtyp='doppelzimmer',
    kapazitaet=3,
    preis_pro_nacht=120.00,
    aktiv=True
)

# Testbuchungen erstellen
heute = date.today()

buchung1 = Booking.objects.create(
    kunde=kunde1,
    raum=raum1,
    check_in=heute,
    check_out=heute + timedelta(days=3),
    anzahl_gaeste=2,
    status='bestaetigt'
)

buchung2 = Booking.objects.create(
    kunde=kunde2,
    raum=raum2,
    check_in=heute + timedelta(days=5),
    check_out=heute + timedelta(days=7),
    anzahl_gaeste=2,
    status='bestaetigt'
)

print("Testdaten erfolgreich erstellt!")
print(f"Kunden: {Customer.objects.count()}")
print(f"Räume: {Room.objects.count()}")
print(f"Buchungen: {Booking.objects.count()}")
"""

if __name__ == "__main__":
    print(__doc__)
    print("\n" + "="*60)
    print("ZUM ERSTELLEN VON TESTDATEN:")
    print("="*60)
    print("Führe folgenden Code in der Django Shell aus:")
    print("python manage.py shell")
    print("\nDann kopiere und füge folgenden Code ein:")
    print("="*60)
    print(TEST_DATA_CREATION)
