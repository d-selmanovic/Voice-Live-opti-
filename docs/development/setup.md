# Einrichtung

Arbeitsverzeichnis: entpackter Ordner activi-agent-core. Python 3.12 oder neuer.

`python3 scripts/validate_project.py` prüft Dokumentverweise, Quellen-/Anforderungszuordnung, Konfigurationsbeispiele und Paketmetadaten ohne Netzwerk und API-Schlüssel.

`PYTHONPATH=src python3 -c 'import activi_agent; print(activi_agent.__version__)'` importiert nur das Skeleton. Ein Voice-Startbefehl existiert in diesem Core noch nicht.

Git-Status mit `git status --short` prüfen. Neue Arbeit auf eigenem Branch fortsetzen. Eine Paketinstallation mit Build-Abhängigkeiten ist getrennt vor dem ersten Core-Release zu prüfen. Der ZIP-Download enthält keine Python-Umgebung.
