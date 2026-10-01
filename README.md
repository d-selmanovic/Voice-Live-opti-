# Activi Agent Core

Wiederverwendbare Basis für Voice-Agenten von Denis Selmanovic / activi.io.

Status: Ordnerstruktur, Arbeitsregeln, Dokumentation und Kundenprojekt-Vorlage eingerichtet. Memory, Wissen, Tools, Telefonie und Browser-Demo sind in dieser Basis noch nicht implementiert. Die bestehende Demo wurde nicht verändert.

Start: AGENTS.md → docs/requirements.md → docs/architecture.md → docs/roadmap.md.

Gemeinsame Funktionen liegen in src/activi_agent/. Die Browser-Testanwendung gehört nach apps/browser-demo/. Für spätere Spezialagenten dient templates/customer-agent/ als Startvorlage. Echte Kundenprojekte bekommen eigene Repositories und geprüfte Basisversionen.

Ein einzelner modularer Server ist der geplante Anfang; separate Dienste oder ein zweiter KI-Agent sind noch nicht festgelegt.

## Lokale Prüfung
`PYTHONPATH=src python -c "import activi_agent; print(activi_agent.__version__)"`

Diese Prüfung importiert nur das Paketgrundgerüst; sie prüft keine Voice-Funktionen.
