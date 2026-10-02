# Lokale Projektprüfung — sofort nutzbar

Voraussetzung: entpacktes activi-agent-core und Python 3.12+. Terminal in diesen Ordner öffnen.

1. `python3 scripts/validate_project.py` ausführen. Erwartung: OK und Anzahl geprüfter Dokumente/Zuordnungen.
2. `PYTHONPATH=src python3 -c 'import activi_agent; print(activi_agent.__version__)'` ausführen. Erwartung: 0.0.0.
3. Bei Link-/Konfigurationsfehlern die benannte Datei korrigieren und Prüfung wiederholen. Bei fehlendem Python passende Umgebung installieren.

Kein Voice-Agent startet damit. Für Browserentwicklung ISS-002 im Tracker. Keine API-Schlüssel nötig.
