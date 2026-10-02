# Rücknahme

Für die aktuelle Dokumentationsarbeit: aus dem Root mit `git log --oneline -5` Änderung bestimmen. Erst sauberen Arbeitsstand mit `git status --short` prüfen. Gewünschte Änderung bei Bedarf durch einen neuen Revert-Commit zurücknehmen; vorhandene uncommittete Arbeit nicht überschreiben. Kein destruktiver Reset erforderlich.

Runtime-Rollback später: vorherige App-/Core-/Konfigurationsversion und Datenbankkompatibilität prüfen; Staging-Rücknahme testen. Datenbankschema nicht blind zurückrollen. Kein bereits erprobter Cloud-Rollback in dieser Basis.
