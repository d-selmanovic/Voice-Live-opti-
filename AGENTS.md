# AGENTS.md – Activi Agent Core

## Ziel und Scope
Wiederverwendbare technische Basis für Voice-Agenten. Diese Einrichtung ist ein Grundgerüst, noch kein funktionsfähiger neuer Voice-Agent. Kundenprojekte verwenden später festgelegte Basisversionen und eigene Repositories. Die bestehende Render-Demo ist Referenz; nicht ohne auftragsbezogene Freigabe umbauen oder veröffentlichen.

## Verbindliche Produktentscheidungen
- Zuerst Browsergespräche vollständig entwickeln und testen; danach Telefonie integrieren.
- Smalltalk ist ausdrücklich erwünscht und muss möglich sein. Längeres Abschweifen freundlich zur Aufgabe zurückführen. Keine harten Themenblockaden für normale Plauderei.
- Laufende Themenkontrolle ist die gewählte Richtung; keine verpflichtende Prüfung jeder Antwort vor Wiedergabe. Bereits hörbare Aussagen lassen sich nicht zurückholen.
- Keine Fakten, Spielergebnisse, persönlichen Erlebnisse oder erfolgreich ausgeführten Aktionen erfinden.
- Jeder Agent hat eigenes Firmenwissen, eigene Kunden-Memory, Tools und Berechtigungen. Die Basis stellt Funktionen bereit, keine gemeinsame Kunden-Memory.
- Gesprächskontext, dauerhaftes Kundenwissen und Firmenwissen getrennt behandeln. Nur ausgewählte nachvollziehbare Informationen dauerhaft speichern.
- Anwendung entwickelt von Denis Selmanovic von activi.io; OpenAI liefert gegebenenfalls KI-Modelle und API. Bei Fragen korrekt unterscheiden.

## Technische Grenzen
- Datenzugriffe nach Projekt/Firma und verifiziertem Kundenkontext im Backend begrenzen. Gesprochene IDs sind keine Autorisierung.
- Tools nur über explizite Freigaben und serverseitige Validierung ausführen. Smalltalk erweitert keine Berechtigungen.
- Keine allgemeine Websuche für spezialisierte Geschäftsagenten ohne ausdrückliche Konfiguration.
- Änderungen mit Außenwirkung gegen doppelte Ausführung absichern. Erforderliche Kundenbestätigung im Workflow prüfen.
- Buchungen und CRM-Änderungen erst nach bestätigtem Erfolg als erledigt melden.
- Audiofluss von langsameren externen Aufgaben trennen; asynchrone Verarbeitung, Zeitlimits und Fehlerbehandlung vorsehen. Zusätzliche KI-Agenten nur bei begründetem Bedarf.
- API, MCP oder Webhooks passend zum jeweiligen Dienst wählen; konkrete Anbindungen sind noch nicht implementiert.
- Secrets, Gesprächsaufzeichnungen, Kunden-Memory und private Wissensdaten niemals in Git speichern.

## Struktur und Arbeit
- Gemeinsame Bibliothek: src/activi_agent/; Browser-Testanwendung: apps/browser-demo/.
- Startvorlage: templates/customer-agent/; Beispiele: examples/; Architekturentscheidungen: docs/decisions/.
- Kundenprojekte auf geprüfte Paketversionen festlegen; Updates ausdrücklich testen, nicht automatisch überall erzwingen.
- Kleine nachvollziehbare Änderungen auf Entwicklungsbranches; passende Prüfungen durchführen und Ergebnisse ehrlich benennen.
- Offizielle Dokumentation und OpenAI Cookbook bei OpenAI-Implementierungsfragen prüfen; aktuelle Fähigkeiten nicht aus alten Chat-Aussagen übernehmen.
- Keine funktionierenden Adapter, Produktionsreife oder bestandenen Sprachtests behaupten, solange sie nicht nachgewiesen sind.
- Anforderungen und Architekturentscheidungen mit Datum in docs/ aktualisieren.
- Bestehende ZIP-Dateien sind historische Referenzen und kein Nachweis des neuesten Live-Codes.
- Ein vorhandenes Backend bedeutet nicht automatisch einen zweiten KI-Agenten; vor solchen Aussagen Code prüfen.
- Für den nächsten Entwicklungsauftrag README.md, docs/requirements.md und docs/roadmap.md lesen.
