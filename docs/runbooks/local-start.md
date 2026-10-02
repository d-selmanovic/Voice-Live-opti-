# Lokal starten

Diese Migration wurde nur lokal geprüft. Render wurde nicht geändert. Auf deinem Mac im Projektordner (Python 3.12+) ausführen:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
./scripts/start-local.sh
```

Dann http://localhost:3000 öffnen. Alternativ nach Installation `.venv/bin/activi-voice` starten. Der Server hört standardmäßig nur auf 127.0.0.1:3000. Bei einem anderen Port APP_ORIGIN passend setzen.

Ein vorhandener OPENAI_API_KEY wird aus der Prozessumgebung oder der privaten `.env.local` im Projektroot gelesen. Bestehenden lokalen Key weiterverwenden; er bleibt ausschließlich im Backend. Ohne Key funktionieren Oberfläche, Konfiguration und Healthcheck; Gesprächsstart meldet eine fehlende Backend-Konfiguration. Keine Schlüssel aus der alten Demo automatisch kopiert. `.env.example` enthält nur Einstellungsnamen. Bewertungen und Tickets liegen standardmäßig in `private-data/browser-demo/`, ausgeschlossen von Git.

Beenden: Ctrl+C. Für Tests:

```bash
ACTIVI_ENV_FILE=/tmp/activi-no-env OPENAI_API_KEY= DATABASE_URL= .venv/bin/python -m unittest discover -s tests -v
python3 scripts/validate_project.py
```

Sprachabnahme auf dem Mac: Stimme/Sprache/Testcode wählen, Mikrofon erlauben, sprechen, unterbrechen, stummschalten, beenden und neu starten; Demo-Ticket bestätigen/ablehnen sowie vor Bestätigung Aufgabe zurücksetzen. Bosnisch, Deutsch und Englisch getrennt hören. Erst nach dieser Abnahme weitere Funktionen/Telefonie.

Die hier ausgeführten HTTP- und Unit-Tests ersetzen diesen Hörtest nicht. Der automatische Cloud-Browserzugriff auf localhost war mit ERR_BLOCKED_BY_CLIENT gesperrt. Das localhost dieser Arbeitsumgebung ist nicht dein Mac. Installation wurde hier editable mit bereits vorhandenen Abhängigkeiten getestet; eine frische macOS-Installation steht aus.
