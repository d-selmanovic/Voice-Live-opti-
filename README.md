# Activi Agent Core

Wiederverwendbare Voice-Agentenbasis von Denis Selmanovic / activi.io.

Status: Browser-Demo migriert (0.1.0), lokal startbar. 15 Tests und localhost-HTTP bestanden. Echtes Sprachgespräch/Mac-Abnahme offen. Kunden-Core, Memory und Integrationen bleiben geplant. Kein Render-Deploy.

[Auf deinem Mac starten](docs/runbooks/local-start.md).

Einstieg: [AGENTS.md](AGENTS.md), [Status](docs/status.md), [Struktur](docs/structure.md), [Anforderungen](docs/requirements.md), [Aufgaben](docs/issues.md).

[Einzelprüfung von 43 Bereichen](docs/audit/structure-review.md) trennt Bedarf, Quellenunterstützung, eigene Entscheidungen und verbleibende praktische Nachweise. [Quellen](docs/sources.md) umfassen offizielle OpenAI-, Python- und GitHub-Dokumentation.

## Lokal prüfen
Aus diesem Ordner mit Python 3.12+: `python3 scripts/validate_project.py`.

Danach optional: `PYTHONPATH=src python3 -c 'import activi_agent; print(activi_agent.__version__)'`.

Das prüft das Grundgerüst, nicht Audioqualität oder produktive Integrationen. Für zukünftige Funktionsentwicklung [Roadmap](docs/roadmap.md) und [Browserplan](apps/browser-demo/README.md) lesen.
