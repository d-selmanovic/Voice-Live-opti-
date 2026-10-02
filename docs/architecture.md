# Architektur — Ist und Ziel

Ist: lokale Referenz voice-agent, Commit fba6401a0019fa70024f85d63ff08e51131a53fc. Browser trägt Audio per WebRTC, der Server erstellt GPT-Live-Sessions und hängt sich per Sideband an. Responses-Delegation ist konfiguriert, Tools werden serverseitig verarbeitet. Dieser Befund ist statisch, kein Live-Test.

Ziel: gleiche klare Trennung als modularer Core. Ein Server zuerst, zusätzliche Dienste nur bei Bedarf. Responses-Delegation als Ausgangspunkt prüfen; Client Delegation erst für eigene Workflows/Ergebnisprüfung entscheiden. Keine pauschale Umstellung nötig.

[System](architecture/diagrams/system.md), [Audio](architecture/diagrams/audio-flow.md), [Tools](architecture/diagrams/tool-flow.md), [Datentrennung](architecture/diagrams/data-isolation.md), [Datenmodell](architecture/data-model.md), [Module](architecture/module-map.md).

Eingaben aus Dokumenten, Tools oder Memory sind Daten, keine Erlaubnis zur Änderung von Geschäftsregeln. Allgemeine Websuche der Referenz nicht ungeprüft übernehmen. Quellen S03/S04/S07/S14 im [Register](sources.md).
