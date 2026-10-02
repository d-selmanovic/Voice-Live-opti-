# Aufgaben und Fehler — führender lokaler Tracker

Status: offen / in Arbeit / blockiert / erledigt. Owner: Entwicklungsagent im freigegebenen Auftrag; fachliche Entscheidungen: Denis. Kein GitHub-Tracker für diesen Core eingerichtet. Bei späterer Migration GitHub-IDs zuordnen und diese Liste als Verzeichnis führen, keine parallele Statuspflege.

## ISS-001: Projektorganisation und Einzelprüfung

Priorität: wichtig. Status: **erledigt**. Anforderungen: REQ-012,REQ-016.

Nächster Schritt / Blockade: Abgeschlossen; weiter mit ISS-002.

Abschlusskriterium: Konsistenz, negative Prüffälle, Git und Download nachgewiesen. Nachweis: docs/audit/validation.json; lokaler Git-Commit und Activi-Agent-Core-Optimiert.zip.

## ISS-002: Aktuellen Referenzstand und Browsermigration prüfen

Priorität: wichtig. Status: **in Arbeit**. Anforderungen: REQ-002,REQ-009.

Nächster Schritt / Blockade: Migration und 15 technische Tests abgeschlossen; jetzt echter Mac-Browser-/Audiotest.

Abschlusskriterium: Browserbasis reproduzierbar gestartet und Verhalten getestet. Nachweis: noch offen.

## ISS-003: Tool-Freigaben und Websuche prüfen

Priorität: wichtig. Status: **offen**. Anforderungen: REQ-007,REQ-008.

Nächster Schritt / Blockade: Demo-Websuche inventarisieren, Agent-Allowlist entwerfen.

Abschlusskriterium: Unerlaubte und doppelte Aktionen technisch abgewiesen. Nachweis: noch offen.

## ISS-004: Individuelle Kunden-Memory und Identifizierung

Priorität: wichtig. Status: **blockiert**. Anforderungen: REQ-004,REQ-005.

Nächster Schritt / Blockade: Q06 vor Implementierung klären.

Abschlusskriterium: Kunden-/Firmengrenzen und Korrektur/Löschung nachgewiesen. Nachweis: noch offen.

## ISS-005: Firmenwissen anbinden

Priorität: wichtig. Status: **offen**. Anforderungen: REQ-006.

Nächster Schritt / Blockade: Quellen- und Freigabevertrag festlegen.

Abschlusskriterium: Antworten nur aus passenden freigegebenen Quellen. Nachweis: noch offen.

## ISS-006: Smalltalk und laufende Kontrolle

Priorität: wichtig. Status: **offen**. Anforderungen: REQ-003.

Nächster Schritt / Blockade: Szenarien für Plauderei und Rückführung umsetzen.

Abschlusskriterium: DE/BS/EN, freundlich, ohne erfundene Fakten geprüft. Nachweis: noch offen.

## ISS-007: Sprachbewertung und Jeff-Kriterien

Priorität: wichtig. Status: **blockiert**. Anforderungen: REQ-011.

Nächster Schritt / Blockade: Q04/Q10 vor Freigabekriterien klären.

Abschlusskriterium: Definiertes Testset, Ergebnisse und Grenzen dokumentiert. Nachweis: noch offen.

## ISS-008: Konfigurationsidentität und Rollen

Priorität: wichtig. Status: **offen**. Anforderungen: REQ-014.

Nächster Schritt / Blockade: Q02/Q03 vor Engine-/Rollenarchitektur klären.

Abschlusskriterium: Identitäten sauber getrennt und Profile geprüft. Nachweis: noch offen.

## ISS-009: Pilotbetrieb und Wiederherstellung

Priorität: wichtig. Status: **blockiert**. Anforderungen: REQ-013,REQ-015.

Nächster Schritt / Blockade: Q05/Q08 und Runtime voraussetzen.

Abschlusskriterium: Staging-Deployment, Rollback und Restore tatsächlich getestet. Nachweis: noch offen.

## ISS-010: Zweites Kundenprofil

Priorität: wichtig. Status: **offen**. Anforderungen: REQ-001.

Nächster Schritt / Blockade: Nach erster Browserbasis eigenes Profil erzeugen.

Abschlusskriterium: Gemeinsamer Core, getrennte Daten und geprüfte Version. Nachweis: noch offen.

## ISS-011: Telefonieadapter

Priorität: später. Status: **blockiert**. Anforderungen: REQ-002.

Nächster Schritt / Blockade: Browserabnahme und Q07 abwarten.

Abschlusskriterium: Echtes Gespräch inkl. Fehler-/Weiterleitungsablauf geprüft. Nachweis: noch offen.

## ISS-012: Private Daten und Logs

Priorität: wichtig. Status: **offen**. Anforderungen: REQ-015.

Nächster Schritt / Blockade: Aufbewahrung und Redaction im Runtimeplan festlegen.

Abschlusskriterium: Keine Secrets/privaten Daten in Git; Löschpfad geprüft. Nachweis: noch offen.
