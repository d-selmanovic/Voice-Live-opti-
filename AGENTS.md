# Activi Agent Core – Arbeitsanweisungen

## Ziel und aktueller Stand
Wiederverwendbare technische Basis für kundenindividuelle Voice-Agenten von Denis Selmanovic / activi.io. Aktuell: Struktur und migrierte Browser-Demo 0.1.0; lokale technische Tests bestanden, echte Sprachabnahme offen. Bestehende Render-Demo ist separate Referenz.

## Einstieg und Pflichtlektüre
Vor Arbeit [Status](docs/status.md), [Anforderungen](docs/requirements.md), [Tracker](docs/issues.md) und [Entwicklungsregeln](docs/development/rules.md) lesen. Relevante Architektur, Guides und Quellen gezielt hinzunehmen. [Strukturübersicht](docs/structure.md) ordnet alle Bereiche zu.

## Verbindliche Entscheidungen
- Browser zuerst entwickeln und prüfen; Telefonie danach.
- Smalltalk ist erwünscht. Längeres Abschweifen freundlich zurückführen; keine erfundenen Fakten oder eigenen Erlebnisse.
- Laufende Kontrolle statt verpflichtender Audioprüfung vor Wiedergabe. Tool-/Datenrechte trotzdem serverseitig erzwingen.
- Firma, Agent, Konfigurationsversion, Session und verifizierten Kundenkontext trennen. Eine ID ist keine Autorisierung.
- Firmenwissen, Kunden-Memory und Gesprächskontext getrennt. Keine gemeinsam genutzten Kundenerinnerungen durch die Basis.
- Werkzeuge explizit erlauben, Argumente prüfen, doppelte Aktionen verhindern und veraltete Ergebnisse verwerfen. Erforderliche Kundenbestätigung prüfen. Erfolg erst nach bestätigter Ausführung melden.
- Allgemeine Websuche für spezialisierte Agenten nur bei ausdrücklicher Freigabe. Demo-Websuche nicht ungeprüft übernehmen.
- Anwendung: Denis Selmanovic von activi.io; verwendete OpenAI-Modelle/API: OpenAI.
- Secrets, private Memory, echte Kundendaten und Aufzeichnungen niemals in Git/Download aufnehmen.

## Arbeitsablauf
Anforderung/Issue zuordnen; Ist-Stand prüfen; einfachste ausreichende Änderung durchführen; passende Prüfungen ausführen; Status und Nachweise pflegen. Fakten, Annahmen, Vorschläge und offene Tests unterscheiden. Quellen bestätigen Prinzipien, nicht jede Ordnerbenennung. Keine Produktionsreife oder erreichten Jeff-Werte ohne Nachweis behaupten.

Für große Änderungen Plan nach [PLANS.md](PLANS.md) führen. Einziger lokaler Tracker: docs/issues.md. Architekturentscheidungen liegen in docs/decisions/. Kunde nutzt später feste geprüfte Core-Version; zusätzliche Agenten/Dienste nur mit begründetem Nutzen.

Bei wesentlichen Unklarheiten eigene zugängliche Quellen zuerst prüfen, dann gezielt fragen. [Offene Fragen](docs/project/open-questions.md) nennen abhängige Phasen. Nicht erneut nach bereits erteilter Freigabe fragen. Eigenständige reversible Arbeiten innerhalb des Auftrags abschließen.

## Prüfbefehle aus dem Projektroot
- `python3 scripts/validate_project.py` — Offline-Konsistenz.
- `PYTHONPATH=src python3 -c 'import activi_agent; print(activi_agent.__version__)'` — nur Paketimport.
- `git diff --check` — Formatfehler im Diff.

Lokaler Start nach docs/runbooks/local-start.md; Tests mit .venv/bin/python -m unittest discover -s tests -v. Bereichsanweisungen: Backend, Frontend und evals besitzen eigene AGENTS.md; bei Änderungen dort ausdrücklich lesen. [Definition of done](docs/development/definition-of-done.md) beachten. Aktuelle API-Dokumentation vor Implementierung prüfen, archivierte Beispiele nicht als aktuelle API übernehmen.
