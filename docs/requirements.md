# Anforderungen

Status: dokumentiert, Laufzeit-Abnahmen noch nicht ausgeführt.

- **REQ-001 — Wiederverwendbare Basis:** Zwei Profile nutzen denselben Core ohne Kopieren seiner Implementierung.
- **REQ-002 — Browser vor Telefonie:** Browserablauf einschließlich Fehlern und Unterbrechungen geprüft, bevor Telefonie umgesetzt wird.
- **REQ-003 — Smalltalk erwünscht:** Kurze Plauderei zulassen; längeres Abschweifen freundlich zurückführen; keine unbelegten Fakten.
- **REQ-004 — Getrennte Daten:** Zugriffe über Firma, Projekt und verifizierten Kundenkontext; fremde Datenzugriffe werden abgewiesen.
- **REQ-005 — Optionale Kunden-Memory:** Lesen, Schreiben, Korrigieren und Löschen nachvollziehbar; ohne Memory brauchbarer Betrieb.
- **REQ-006 — Individuelles Firmenwissen:** Quelle, Version, Freigabe und Firmenzuordnung prüfen; bei Wissenslücken keine Erfindungen.
- **REQ-007 — Begrenzte Tools:** Server prüft erlaubtes Tool, Argumente und Identität; Schreiben nur mit erforderlicher Bestätigung.
- **REQ-008 — Zuverlässige Aktionen:** Doppelte Aufrufe bewirken keine Doppelaktion; verspätete Ergebnisse ändern keine überholte Aufgabe.
- **REQ-009 — Flüssiger Audiofluss:** Audio und Backendarbeit separat messen; Unterbrechung, langsame Tools und Fehler im Gespräch testen.
- **REQ-010 — Korrekte Herkunft:** Denis Selmanovic / activi.io als Anwendungsentwickler; OpenAI als Modell-/API-Anbieter unterscheiden.
- **REQ-011 — Nachvollziehbare Evaluation:** Gesprochenes Anliegen, Delegation, Tool-Ergebnis, Endzustand und Antwort verbunden auswerten.
- **REQ-012 — Dauerhafte Projektführung:** Regeln, Aufgaben, Entscheidungen und Nachweise aus Dateien ohne Chat nachvollziehbar.
- **REQ-013 — Versionen und Betrieb:** Core-Updates getestet; Start, Rücknahme und Wiederherstellung nachgewiesen.
- **REQ-014 — Konfiguration statt Agentenkopien:** Agent-, Konfigurations-, Session- und Kundenidentität getrennt; Profil ist keine eigene Modellinstanz.
- **REQ-015 — Vertrauliche Inhalte:** Keine Secrets, privaten Memorys, Aufzeichnungen oder echten Kundendaten in Git/ZIP.
- **REQ-016 — Ehrliche Evidenz:** Dokumentiert, implementiert, ausgeführt und getestet ausdrücklich unterscheiden.

[Einzelprüfung](audit/structure-review.md) · [Aufgabenregister](issues.md) · [Offene Fragen](project/open-questions.md)
