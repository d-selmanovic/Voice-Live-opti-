# Einzelprüfung und Optimierung

Stand 02.10.2026. Jeder vorher vorgeschlagene Bereich wurde auf Bedarf, Quellenunterstützung, Alternative und verbleibenden praktischen Nachweis bewertet. Konkrete Ordnernamen sind unsere Ableitung, keine OpenAI-Norm. Kein mathematischer Optimalitätsnachweis und keine Produktionsfreigabe.

## A01: Zentrale AGENTS.md

Anforderungen: REQ-012, REQ-016. Quellen: S01. Evidenz: direkt.

Entscheidung: **jetzt**. Kompakter Einstieg und explizite Lesepflichten.

Alternative: Alle Details in einer langen Datei erzeugen Kontextlast.

Ziel: `AGENTS.md`. Noch nachzuweisen: Anweisungsentdeckung im konkreten Mac/Codex-Setup später prüfen.

## A02: Bereichs-AGENTS.md

Anforderungen: REQ-012. Quellen: S01. Evidenz: direkt.

Entscheidung: **jetzt**. Nur Frontend, Backend und Evals brauchen eigene Regeln.

Alternative: Eine Datei je Ordner wäre redundant.

Ziel: `apps/browser-demo/backend/AGENTS.md`. Noch nachzuweisen: Bereichsregeln auf Widersprüche prüfen.

## A03: Ziel und Umfang

Anforderungen: REQ-001, REQ-012. Quellen: S12. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Erste Basis und späterer visueller Builder ausdrücklich trennen.

Alternative: Name Voice Builder allein legt keine UI fest.

Ziel: `docs/project/vision.md`. Noch nachzuweisen: Umfang mit späteren Entwicklungsaufträgen abgleichen.

## A04: Anforderungen

Anforderungen: REQ-012, REQ-016. Quellen: S05. Evidenz: abgeleitet.

Entscheidung: **jetzt**. IDs mit Abnahmekriterium verbinden Audit und Aufgaben.

Alternative: Lose Chat-Aussagen sind kein prüfbarer Projektstand.

Ziel: `docs/requirements.md`. Noch nachzuweisen: Verknüpfung validieren; Laufzeitabnahmen noch offen.

## A05: Status

Anforderungen: REQ-012, REQ-016. Quellen: S02. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Aktuellen Stand und Evidenz getrennt führen.

Alternative: Roadmap allein enthält keine Nachweise.

Ziel: `docs/status.md`. Noch nachzuweisen: Nach jeder wesentlichen Arbeit aktualisieren.

## A06: Offene Fragen

Anforderungen: REQ-014, REQ-016. Quellen: Nutzeranforderung. Evidenz: Nutzeranforderung.

Entscheidung: **jetzt**. Engine-ID, Parallelität und Qualitätsziel nicht erfinden.

Alternative: Alle Entwicklung wegen späterer Telefonie blockieren.

Ziel: `docs/project/open-questions.md`. Noch nachzuweisen: Vor jeweils abhängigen Phasen klären.

## A07: Regeln und Fertigkriterien

Anforderungen: REQ-012, REQ-016. Quellen: S01, S02. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Entwicklungsregeln und Laufzeitregeln unterscheiden.

Alternative: Alles als Voice-Prompt formulieren wäre falsch.

Ziel: `docs/development/rules.md`. Noch nachzuweisen: Befehle und Definition-of-done tatsächlich prüfen.

## A08: Roadmap

Anforderungen: REQ-002, REQ-012. Quellen: S02. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Phasen und Übergangskriterien darstellen.

Alternative: Roadmap als konkurrierende To-do-Liste.

Ziel: `docs/roadmap.md`. Noch nachzuweisen: Jede Phase hat beobachtbare Abnahme.

## A09: Backlog/Issues/To-dos

Anforderungen: REQ-012. Quellen: S12. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Ein lokaler Tracker ist führend; später GitHub übernehmen.

Alternative: Zusätzlicher planning/backlog.md würde doppelte Pflege erzeugen.

Ziel: `docs/issues.md`. Noch nachzuweisen: Stabile IDs, Status, nächste Schritte und Nachweis prüfen.

## A10: Ausführungspläne

Anforderungen: REQ-012. Quellen: S02. Evidenz: direkt.

Entscheidung: **jetzt**. Für Migration und große Änderungen, nicht jede Kleinkorrektur.

Alternative: Eine Checkliste ohne Kontext und Rücknahmeplan reicht nicht.

Ziel: `PLANS.md`. Noch nachzuweisen: Aktuellen Plan bis Ergebnis und Erkenntnissen pflegen.

## A11: GitHub Vorlagen

Anforderungen: REQ-012. Quellen: S12. Evidenz: direkt.

Entscheidung: **jetzt**. Lokale Issue- und PR-Vorlagen vorbereiten.

Alternative: GitHub-Projekt jetzt ungefragt erzeugen.

Ziel: `.github/ISSUE_TEMPLATE/bug.md`. Noch nachzuweisen: Nutzung nach neuer Repository-Veröffentlichung prüfen.

## A12: Automatische Prüfungen

Anforderungen: REQ-012, REQ-016. Quellen: S12. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Offline-Projektintegrität in lokalem Skript und CI-Beschreibung.

Alternative: Grüne CI als bestandene Voice-Evaluation ausgeben.

Ziel: `.github/workflows/project-checks.yml`. Noch nachzuweisen: Workflow lokal parsen; GitHub-Ausführung erst nach Push nachweisen.

## A13: Architektur und Modulkarte

Anforderungen: REQ-001, REQ-009. Quellen: S03, S04. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Ist-Referenz und geplanten Core getrennt beschreiben.

Alternative: Ein Zielbild als bereits laufende Architektur zeichnen.

Ziel: `docs/architecture.md`. Noch nachzuweisen: Codefluss statisch prüfen; End-to-End-Messung später.

## A14: Architekturentscheidungen

Anforderungen: REQ-012. Quellen: S02. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Kontext, Alternativen, Nachteile und Neubewertung erfassen.

Alternative: Entscheidungen bei jedem Chat neu treffen.

Ziel: `docs/decisions/0002-organization.md`. Noch nachzuweisen: Jede wesentliche Änderung auf neue Erkenntnisse zurückführen.

## A15: Systemzeichnung

Anforderungen: REQ-009, REQ-012. Quellen: S03, S04. Evidenz: abgeleitet.

Entscheidung: **jetzt**. System mit Audio- und Steuerverbindungen zeigen.

Alternative: Diagramm ohne Statuskennzeichnung.

Ziel: `docs/architecture/diagrams/system.md`. Noch nachzuweisen: Mit Referenzcode vergleichen; keine Live-Verifikation behaupten.

## A16: Audiozeichnung

Anforderungen: REQ-009. Quellen: S04, S14. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Audiowiedergabe ist nicht gleich erzeugtes Transkript.

Alternative: Sideband als Audio-Vorabkontrolle darstellen.

Ziel: `docs/architecture/diagrams/audio-flow.md`. Noch nachzuweisen: Hörbare Antwortzeiten und Unterbrechungen später messen.

## A17: Tool-Zeichnung

Anforderungen: REQ-007, REQ-008. Quellen: S04, S07, S16. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Autorisierung, Revision und eindeutigen Executor abbilden.

Alternative: Nur Prompt-Regeln einsetzen.

Ziel: `docs/architecture/diagrams/tool-flow.md`. Noch nachzuweisen: Doppelte, unzulässige und verspätete Aufrufe praktisch testen.

## A18: Datentrennung und Datenmodell

Anforderungen: REQ-004, REQ-014. Quellen: S06. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Eigene firmenspezifische Server-Zuordnung vorschlagen.

Alternative: Repositories als Zugriffsschutz behandeln.

Ziel: `docs/architecture/data-model.md`. Noch nachzuweisen: Angriffe auf fremde Kunden-/Firmendaten testen.

## A19: Guides

Anforderungen: REQ-001, REQ-012. Quellen: S12. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Konkrete Arbeitsabläufe und gegenwärtige Grenzen dokumentieren.

Alternative: Tutorials mit nicht existierenden Befehlen liefern.

Ziel: `docs/guides/new-agent.md`. Noch nachzuweisen: Zweites Projekt nach Anleitung später tatsächlich erzeugen.

## A20: Quellenregister

Anforderungen: REQ-016. Quellen: S01. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Quelle, Datum, Aussage und Grenze je Entscheidung.

Alternative: Alle Ordner als offiziell vorgeschrieben ausgeben.

Ziel: `docs/sources.md`. Noch nachzuweisen: Quellen beim nächsten Implementierungsschritt erneut auf Aktualität prüfen.

## A21: Runbooks

Anforderungen: REQ-013. Quellen: S09. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Praktische lokale Prüfungen jetzt; Deployment-Gates offen kennzeichnen.

Alternative: Ungetestete Cloud-Befehle als fertiges Runbook liefern.

Ziel: `docs/runbooks/local-start.md`. Noch nachzuweisen: Lokale Anleitung ausführen; Cloud/Restore erst nach Implementierung.

## A22: Security und Datenhaltung

Anforderungen: REQ-004, REQ-015. Quellen: S07, S09. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Datenminimierung und Zugriff an konkreten Grenzen dokumentieren.

Alternative: Allgemeine Checkliste ohne Implementierungsbezug.

Ziel: `docs/security/access-control.md`. Noch nachzuweisen: Isolation, Löschung und Logs in Pilotumgebung testen.

## A23: Sprachbewertung

Anforderungen: REQ-011. Quellen: S05. Evidenz: direkt.

Entscheidung: **jetzt**. Evals von technischen Unit-Tests trennen.

Alternative: 13 Python-Tests als Sprachqualitätsnachweis.

Ziel: `docs/evaluation/strategy.md`. Noch nachzuweisen: DE/BS/EN, Unterbrechung und Toolfehler evaluieren.

## A24: 80-Prozent-Ziel

Anforderungen: REQ-011, REQ-016. Quellen: S05. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Bedeutung und Datensatz offen; frühere Jeff-Anforderung nicht pauschal übertragen.

Alternative: Eine frei erfundene Gesamtmetrik festschreiben.

Ziel: `docs/evaluation/release-criteria.md`. Noch nachzuweisen: Mit Nutzer Kategorien, Samplegröße und Schwellen festlegen.

## A25: Technische Tests

Anforderungen: REQ-007, REQ-008. Quellen: S05. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Testtypen beschreiben; Tests erst zusammen mit tatsächlichen Funktionen.

Alternative: Leere unit/integration/contract-Bäume als Abdeckung darstellen.

Ziel: `tests/README.md`. Noch nachzuweisen: Verhaltens- und Integrationstests im Entwicklungsauftrag ausführen.

## A26: src-Paketlayout

Anforderungen: REQ-001. Quellen: S10, S11. Evidenz: direkt.

Entscheidung: **behalten**. Gemeinsame Python-Bibliothek von Apps trennen.

Alternative: Flaches Demo-Layout ist einfacher, weniger klar bei Paketverteilung.

Ziel: `pyproject.toml`. Noch nachzuweisen: Paketimport jetzt; Wheel-Installation und Abhängigkeiten vor Release.

## A27: Browser-App

Anforderungen: REQ-002, REQ-009. Quellen: S03, S04. Evidenz: abgeleitet.

Entscheidung: **behalten**. Vor Telefonie einen reproduzierbaren Browserablauf.

Alternative: Parallel mehrere Telefonieadapter entwickeln.

Ziel: `apps/browser-demo/README.md`. Noch nachzuweisen: Migration und echtes Sprachgespräch noch erforderlich.

## A28: Kundenprojekt-Vorlage

Anforderungen: REQ-001, REQ-014. Quellen: S11. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Startvorlage benennt fehlende Core-Veröffentlichung und Konfigurationsstatus.

Alternative: Kompletten Core in jedes Repo kopieren.

Ziel: `templates/customer-agent/README.md`. Noch nachzuweisen: Zweites isoliertes Profil nach Core-Release prüfen.

## A29: Beispiele

Anforderungen: REQ-001. Quellen: S12. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Ein gültiges bereinigtes Profil jetzt; lauffähige Agenten später.

Alternative: Leere Beispiele als nutzbare Voice-Agenten ausgeben.

Ziel: `examples/basic-agent/agent.example.json`. Noch nachzuweisen: JSON prüfen; Runtime-Verhalten später.

## A30: Hilfsskripte

Anforderungen: REQ-012, REQ-016. Quellen: S02. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Projektintegrität ohne Cloud/API prüfen.

Alternative: Tests für nicht existierende Laufzeitfunktionen.

Ziel: `scripts/validate_project.py`. Noch nachzuweisen: Prüfer auch mit absichtlich beschädigter Kopie testen.

## A31: Deployment

Anforderungen: REQ-013. Quellen: S09. Evidenz: abgeleitet.

Entscheidung: **später**. Nach Browserreife passende Hosting-Konfiguration.

Alternative: Bestehendes Render ungefragt umbauen.

Ziel: `deploy/README.md`. Noch nachzuweisen: Staging-Deploy und Rücknahme nachweisen.

## A32: Datenbankmigrationen

Anforderungen: REQ-005, REQ-013. Quellen: S06. Evidenz: abgeleitet.

Entscheidung: **später**. Vor Schemaentscheidung nur Anforderungen, kein künstliches migrations-Verzeichnis.

Alternative: Dummy-Migrationen ohne Datenmodell.

Ziel: `docs/security/memory-lifecycle.md`. Noch nachzuweisen: Migration und Restore auf Wegwerfdaten prüfen.

## A33: runtime-Modul

Anforderungen: REQ-008, REQ-009. Quellen: S14. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Lifecycle-Verantwortung dokumentieren, Implementierung im nächsten Auftrag.

Alternative: Aufgabenführung unklar über alle Module verteilen.

Ziel: `src/activi_agent/runtime/README.md`. Noch nachzuweisen: Sessionabschluss, Fehler und verspätete Arbeit testen.

## A34: Observability-Modul

Anforderungen: REQ-009, REQ-011. Quellen: S08, S14. Evidenz: abgeleitet.

Entscheidung: **jetzt**. IDs, Zeiten und technische Ergebnisse ohne Secrets.

Alternative: SDK-Tracing ohne SDK als aktiv annehmen.

Ziel: `src/activi_agent/observability/README.md`. Noch nachzuweisen: Erzeugung, Empfang und tatsächliches Playback unterscheiden.

## A35: Konfigurationsmodul

Anforderungen: REQ-014. Quellen: S11. Evidenz: abgeleitet.

Entscheidung: **jetzt**. Beispielvertrag und getrennte Identitäten dokumentieren.

Alternative: Engine-ID als Authentifizierung nutzen.

Ziel: `src/activi_agent/config/README.md`. Noch nachzuweisen: Ungültige Konfiguration vor Sessionstart künftig abweisen.

## A36: Prompts-Modul

Anforderungen: REQ-003, REQ-010. Quellen: S13. Evidenz: direkt.

Entscheidung: **jetzt**. Kurze Voice-Bausteine; detaillierte Abläufe im Backend.

Alternative: Entwicklungs-AGENTS.md ins Sprachmodell laden.

Ziel: `src/activi_agent/prompts/README.md`. Noch nachzuweisen: Smalltalk, Herkunft und bestätigte Aktionen gesprochen testen.

## A37: Memory-Modul

Anforderungen: REQ-005. Quellen: S06, S15. Evidenz: abgeleitet.

Entscheidung: **behalten**. Gesprächskontext und dauerhafte Kundeninformationen separat.

Alternative: Alles ungeprüft dauerhaft merken.

Ziel: `src/activi_agent/memory/README.md`. Noch nachzuweisen: Herkunft, Konflikte, TTL und Löschung testen.

## A38: Knowledge-Modul

Anforderungen: REQ-006. Quellen: S06. Evidenz: abgeleitet.

Entscheidung: **behalten**. Freigegebene firmenspezifische Quellen, keine beliebige Recherche.

Alternative: Allgemeine Websuche als Firmenwissen behandeln.

Ziel: `src/activi_agent/knowledge/README.md`. Noch nachzuweisen: Falsche Firma, fehlende Quelle und Dokument-Prompt-Injection testen.

## A39: Policies-Modul

Anforderungen: REQ-003, REQ-007. Quellen: S04, S07. Evidenz: abgeleitet.

Entscheidung: **behalten**. Freundliche Rückführung und harte Aktionsgrenzen separat.

Alternative: Smalltalk als Policy-Verstoß werten.

Ziel: `src/activi_agent/policies/README.md`. Noch nachzuweisen: Falsch positive Themenkontrolle und erlaubte Plauderei testen.

## A40: Connector-Modul

Anforderungen: REQ-007, REQ-013. Quellen: S03, S16. Evidenz: abgeleitet.

Entscheidung: **behalten**. API/MCP/Webhook erst anhand des Dienstes wählen.

Alternative: Ein Protokoll für alle Audio- und Geschäftsfunktionen erzwingen.

Ziel: `src/activi_agent/connectors/README.md`. Noch nachzuweisen: Auth, Timeout, Retry und Dienstvertrag praktisch testen.

## A41: Skills/Rollen/Engine-ID

Anforderungen: REQ-014, REQ-016. Quellen: S01. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Bestand inventarisieren; Engine-ID und virtuelle Agenten bleiben ungeklärt.

Alternative: Weitere Modelle oder Skill-Runtime erfinden.

Ziel: `docs/skills.md`. Noch nachzuweisen: Begriffe vor abhängiger Implementierung klären.

## A42: OpenMined/Developer Plugin

Anforderungen: REQ-016. Quellen: S17. Evidenz: abgeleitet.

Entscheidung: **angepasst**. Kein nachgewiesener OpenMined-Bedarf; OpenAI-Dokumentation direkt gelesen.

Alternative: Plugin-Installation ohne verfügbare Statusprüfung behaupten.

Ziel: `docs/project/open-questions.md`. Noch nachzuweisen: Konkretes OpenMined-Produkt bei tatsächlichem Integrationsauftrag nennen.

## A43: Versionsupdates und Abhängigkeiten

Anforderungen: REQ-001, REQ-013. Quellen: S10, S11. Evidenz: abgeleitet.

Entscheidung: **angepasst**. 0.0.0 bleibt Skeleton; feste Kundenabhängigkeit erst nach geprüftem Release.

Alternative: Jetzt eine nicht existierende Paketversion installieren.

Ziel: `docs/development/releases.md`. Noch nachzuweisen: Abhängigkeiten festlegen, Installation/Upgrade testen und Lizenzentscheidung treffen.

Quellen: [Register](../sources.md). Anforderungen: [Liste](../requirements.md). Maschinenlesbare Prüfung: [Matrix](structure-review.json).
