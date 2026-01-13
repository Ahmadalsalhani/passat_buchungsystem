# UpdateV2 - Schnellstart-Anleitung

## 🚀 Erste Schritte

### 1. Server starten

Öffnen Sie ein Terminal und navigieren Sie zum Projektverzeichnis:

```bash
cd c:\Users\ahmad\Desktop\MA\neue_python_Project\passat_buchungsystem-main
```

Aktivieren Sie die virtuelle Umgebung (falls noch nicht aktiv):

```bash
venv\Scripts\activate
```

Starten Sie den Django-Entwicklungsserver:

```bash
python manage.py runserver
```

Der Server läuft jetzt unter: **http://localhost:8000**

### 2. Im Browser öffnen

Öffnen Sie Ihren Webbrowser und gehen Sie zu:
```
http://localhost:8000
```

Melden Sie sich mit Ihren Admin-Zugangsdaten an.

## 📅 Kalenderübersicht verwenden

### Zugriff:
1. Nach dem Login sehen Sie das Dashboard
2. Klicken Sie in der linken Navigation auf **"Kalender Übersicht"**
3. Sie sehen nun den Kalender für den aktuellen Monat

### Funktionen:
- **Navigation:** Nutzen Sie die Buttons "Vorheriger Monat", "Heute" und "Nächster Monat"
- **Räume:** Jede Zeile zeigt einen Raum
- **Tage:** Jede Spalte zeigt einen Tag
- **Farben:** 
  - 🟢 Grün = Raum ist frei
  - ⬜ Grau = Raum ist belegt
- **Buchungen:** Farbige Badges zeigen Kundennamen
- **Details:** Klicken Sie auf eine Buchung für mehr Informationen
- **Tabelle:** Unter dem Kalender finden Sie eine Liste aller Buchungen

## 🔍 Autocomplete verwenden

### Neue Buchung mit Suchfunktion:

1. Klicken Sie auf **"Buchungen"** → **"Neue Buchung"**
2. Im Feld **"Kunde"**:
   - Beginnen Sie zu tippen (min. 2 Buchstaben)
   - Es erscheint eine Liste mit passenden Kunden
   - Wählen Sie den gewünschten Kunden aus
   - Sie können nach Vor-/Nachname oder Kundennummer suchen

3. Im Feld **"Raum"**:
   - Beginnen Sie zu tippen (min. 1 Buchstabe)
   - Es erscheint eine Liste mit passenden Räumen
   - Wählen Sie den gewünschten Raum aus
   - Sie können nach Raumnummer oder Raumname suchen

4. Füllen Sie die restlichen Felder aus
5. Klicken Sie auf **"Speichern"**

## 🎨 Farbsystem verstehen

### Im Kalender:
- Jeder Kunde bekommt automatisch eine eigene Farbe zugewiesen
- Wenn mehrere Kunden am selben Tag in verschiedenen Räumen sind, sehen Sie verschiedene Farben
- Die Farben bleiben konsistent während einer Sitzung

### Beispiel:
```
Raum 101: [Max Mustermann - Rot] [Anna Schmidt - Blau]
Raum 102: [Anna Schmidt - Blau]
```
→ Anna Schmidt hat in beiden Räumen die gleiche Farbe (Blau)

## 💡 Tipps & Tricks

### Kalenderübersicht:
- **Schnellnavigation:** Klicken Sie auf "Heute" um zum aktuellen Monat zurückzukehren
- **Übersicht:** Die Tabelle unter dem Kalender zeigt alle Buchungsdetails
- **Hover:** Fahren Sie mit der Maus über eine Buchung für Zusatzinformationen

### Autocomplete:
- **Schneller tippen:** Je mehr Buchstaben, desto genauer die Suche
- **Kundennummer:** Sie können auch direkt die ID-Nummer eingeben
- **Löschen:** Klicken Sie auf das ❌ Symbol um die Auswahl zu löschen

### Beste Arbeitsweise:
1. **Morgens:** Kalenderübersicht öffnen um Überblick zu bekommen
2. **Buchung erstellen:** Autocomplete nutzen für schnelle Eingabe
3. **Prüfen:** Zurück zum Kalender um Belegung zu verifizieren

## 🛠️ Problemlösung

### Kalender zeigt keine Daten:
- Überprüfen Sie, ob Buchungen für den ausgewählten Monat existieren
- Navigieren Sie zu einem anderen Monat
- Erstellen Sie Testbuchungen

### Autocomplete funktioniert nicht:
- Überprüfen Sie Ihre Internetverbindung (für CDN)
- Laden Sie die Seite neu (F5)
- Löschen Sie Browser-Cache
- Überprüfen Sie Browser-Konsole (F12) auf Fehler

### Fehlende Räume/Kunden:
- Nur **aktive** Räume werden angezeigt
- Erstellen Sie ggf. neue Räume/Kunden im Admin-Bereich

### Server startet nicht:
```bash
# Prüfen Sie, ob Port 8000 bereits belegt ist
# Verwenden Sie einen anderen Port:
python manage.py runserver 8080
```

## 📊 Testdaten erstellen

Falls Sie das System testen möchten, erstellen Sie Testdaten:

```bash
python manage.py shell
```

Dann kopieren und fügen Sie den Code aus `test_updatev2.py` ein.

## 🎯 Häufige Aufgaben

### Neue Buchung mit Kalender-Check:
1. Öffnen Sie Kalenderübersicht
2. Prüfen Sie freie Räume für gewünschtes Datum
3. Klicken Sie auf "Buchungen" → "Neue Buchung"
4. Nutzen Sie Autocomplete für Kunde und Raum
5. Geben Sie Daten ein
6. Speichern
7. Zurück zum Kalender → Buchung sollte erscheinen

### Überlappende Buchungen vermeiden:
1. Vor jeder Buchung: Kalender öffnen
2. Prüfen Sie den gewünschten Zeitraum
3. Graue Felder = Raum ist belegt
4. Grüne Felder = Raum ist frei
5. Wählen Sie einen freien Raum

### Monatsübersicht drucken:
1. Öffnen Sie Kalenderübersicht
2. Wählen Sie den gewünschten Monat
3. Drücken Sie Strg+P (Windows) oder Cmd+P (Mac)
4. Drucken oder als PDF speichern

## 📞 Support

Bei weiteren Fragen:
- Lesen Sie die ausführliche Dokumentation in `UpdateV2_Features.md`
- Konsultieren Sie die Implementierungs-Details in `IMPLEMENTATION_SUMMARY.md`
- Verwenden Sie die Test-Checkliste in `test_updatev2.py`

## ✅ Checkliste für den Start

- [ ] Server gestartet
- [ ] Im Browser angemeldet
- [ ] Kalenderübersicht geöffnet
- [ ] Navigation getestet
- [ ] Neue Buchung mit Autocomplete erstellt
- [ ] Buchung im Kalender gefunden

**Viel Erfolg mit dem Passat Buchungssystem UpdateV2!** 🎉
