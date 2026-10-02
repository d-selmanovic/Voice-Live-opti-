# Projektstruktur und Zuständigkeiten

- `AGENTS.md` — verbindliche Arbeitsanweisung und Lesepflichten
- `PLANS.md` — Regeln für ausführliche Entwicklungspläne
- `planning/plans/` — Ausführungspläne; kein zweiter Aufgaben-Tracker
- `docs/issues.md` — einzige führende lokale Aufgaben-/Fehlerliste
- `docs/requirements.md` — Anforderungs-IDs und Abnahme
- `docs/status.md` — belegter aktueller Stand
- `docs/project/` — Ziel, Scope, offene Fragen
- `docs/development/` — Regeln, Start, Prüfungen und Releases
- `docs/architecture.md` — Ist-/Zielarchitektur
- `docs/architecture/` — Modulkarte, Datenmodell und Diagramme
- `docs/decisions/` — Architekturentscheidungen
- `docs/guides/` — Wiederverwendung und Erweiterungen
- `docs/references/` — Quellenmetadaten
- `docs/runbooks/` — Betriebsabläufe mit ausgewiesenem Gültigkeitsbereich
- `docs/security/` — Datenzugriff und Memory-Lebenszyklus
- `docs/evaluation/` — Sprachqualität und Release-Kriterien
- `docs/audit/` — Einzelprüfung, Quellen-/Anforderungszuordnung und Evidenz
- `docs/skills.md` — Inventar von Entwicklungs- und Runtime-Fähigkeiten
- `src/activi_agent/` — gemeinsame Bibliothek mit noch geplanten Modulen
- `apps/browser-demo/` — noch nicht migrierte Browser-Testanwendung
- `templates/customer-agent/` — Kundenprojekt-Vorlage
- `examples/` — synthetische Konfigurationsbeispiele
- `tests/` — technische Prüfungen im nächsten Implementierungsschritt
- `evals/` — Szenarien; kein bereits laufender Voice-Harness
- `scripts/` — ausführbare Offline-Hilfsskripte
- `deploy/` — vorläufige Betriebskriterien, kein aktives Hosting
- `.github/` — lokale Issue-/PR-/CI-Vorlagen

Keine zusätzliche planning/backlog.md: [docs/issues.md](issues.md) führt Aufgaben. Keine Datenbankmigrationen vor Schemaentscheidung. Bestehende Einstiegspfade bleiben erhalten.
