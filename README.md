# Passat Buchungssystem

Ein vollständiges internes Buchungssystem mit Python und Django zur Verwaltung von Kunden, Buchungen und Rechnungen.

## Features

### Benutzerverwaltung
- Erweitertes User-Model mit Rollen (Admin/User)
- Login/Logout-Funktionalität
- Rollenbasierte Zugriffskontrolle

### Kundenverwaltung
- Vollständige Kundendaten (Anrede, Name, Kontakt, Adresse)
- Kunden anlegen, bearbeiten, löschen
- Suchfunktion

### Raumverwaltung
- Raumtypen: Einzelzimmer, Doppelzimmer, Suite, Konferenzraum
- Kapazität und Preisgestaltung
- Aktiv/Inaktiv Status

### Buchungsverwaltung
- Buchungen mit Kunden und Räumen verknüpfen
- Automatische Berechnung von Nächten und Gesamtpreis
- Validierung (Check-out nach Check-in, Kapazitätsprüfung)
- Dashboard mit Statistiken
- Status-Management (Ausstehend, Bestätigt, Storniert, Abgeschlossen)

### Rechnungsverwaltung
- Automatische Rechnungsnummer-Generierung (INV-00001)
- MwSt.-Berechnung (Standard 19%)
- PDF-Generierung mit ReportLab
- Status-Management (Entwurf, Versendet, Bezahlt, Storniert)

## Technologie-Stack

- **Django 5.0** - Web Framework
- **Python 3.12** - Programmiersprache
- **SQLite** - Datenbank (Entwicklung)
- **Bootstrap 5** - Frontend Framework
- **ReportLab** - PDF-Generierung
- **django-crispy-forms** - Formular-Styling

## Installation

### Voraussetzungen

- Python 3.12 oder höher
- pip (Python Package Manager)
- virtualenv (empfohlen)

### Schritt-für-Schritt Anleitung

1. **Repository klonen**
```bash
git clone https://github.com/Ahmadalsalhani/passat_buchungsystem.git
cd passat_buchungsystem
```

2. **Virtuelle Umgebung erstellen und aktivieren**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Dependencies installieren**
```bash
pip install -r requirements.txt
```

4. **Umgebungsvariablen konfigurieren**
```bash
# Kopieren Sie .env.example zu .env
cp .env.example .env

# Bearbeiten Sie .env und setzen Sie Ihre Werte
# Besonders wichtig: SECRET_KEY
```

5. **Datenbank migrieren**
```bash
python manage.py migrate
```

6. **Superuser erstellen**
```bash
python manage.py createsuperuser
```
Folgen Sie den Anweisungen und erstellen Sie einen Admin-Benutzer.

7. **Server starten**
```bash
python manage.py runserver
```

8. **Browser öffnen**
```
http://127.0.0.1:8000/
```

## Verwendung

### Erste Schritte

1. **Anmelden**: Verwenden Sie die Superuser-Anmeldedaten
2. **Admin-Bereich**: Besuchen Sie `/admin/` für erweiterte Verwaltung
3. **Dashboard**: Übersicht über alle Buchungen und Statistiken

### Workflow

1. **Kunden anlegen**: Navigieren Sie zu "Kunden" → "Neuer Kunde"
2. **Räume anlegen**: Navigieren Sie zu "Räume" → "Neuer Raum"
3. **Buchung erstellen**: Navigieren Sie zu "Buchungen" → "Neue Buchung"
   - Wählen Sie Kunde und Raum
   - Geben Sie Check-in und Check-out Datum ein
   - Anzahl der Gäste eingeben
4. **Rechnung erstellen**: Von der Buchungsdetailseite → "Rechnung erstellen"
5. **PDF herunterladen**: Von der Rechnungsdetailseite → "PDF herunterladen"

## Projekt-Struktur

```
passat_buchungsystem/
├── accounts/          # Benutzerverwaltung
├── customers/         # Kundenverwaltung
├── rooms/             # Raumverwaltung
├── bookings/          # Buchungsverwaltung
├── invoices/          # Rechnungsverwaltung
├── templates/         # HTML Templates
├── static/            # CSS, JS, Bilder
├── media/             # Hochgeladene Dateien
├── manage.py          # Django Management Script
└── requirements.txt   # Python Dependencies
```

## Features im Detail

### Dashboard
- Gesamte Buchungen
- Ausstehende Buchungen
- Bestätigte Buchungen
- Gesamte Kunden
- Letzte Buchungen

### Validierungen
- Check-out muss nach Check-in sein
- Gästeanzahl darf Raumkapazität nicht überschreiten
- E-Mail-Format-Validierung
- Pflichtfelder

### PDF-Rechnung
- Professionelles Layout
- Firmeninformationen
- Kundenadresse
- Buchungsdetails in Tabellenform
- MwSt.-Berechnung
- Gesamtsumme

## Sicherheit

- Login erforderlich für alle Funktionen
- Rollenbasierte Zugriffskontrolle
- CSRF-Protection
- Password Validation
- XSS-Protection

## Entwicklung

### Tests ausführen
```bash
python manage.py test
```

### Statische Dateien sammeln (Produktion)
```bash
python manage.py collectstatic
```

### Neue Migration erstellen
```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment

Für Produktionsumgebungen:

1. Setzen Sie `DEBUG = False` in settings.py
2. Konfigurieren Sie eine Produktions-Datenbank (PostgreSQL empfohlen)
3. Verwenden Sie einen WSGI-Server (z.B. Gunicorn)
4. Setzen Sie einen Reverse-Proxy (z.B. Nginx)
5. Verwenden Sie HTTPS
6. Sammeln Sie statische Dateien mit `collectstatic`

## Lizenz

Dieses Projekt ist Teil einer Masterarbeit.

## Kontakt

Bei Fragen oder Problemen, erstellen Sie bitte ein Issue im Repository.

## Changelog

### Version 1.0.0 (Januar 2026)
- Initiale Version
- Vollständige CRUD-Funktionalität für alle Module
- Dashboard mit Statistiken
- PDF-Rechnungsgenerierung
- Responsive Design mit Bootstrap 5
