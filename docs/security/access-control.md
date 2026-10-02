# Zugriffsvertrag — vor Runtime-Übernahme umsetzen

Identität aus authentifiziertem Serverkontext ableiten. Agenten-Konfigurationswerte oder gesprochene Kundenkennungen autorisieren keine Datenabfrage. Bei fehlendem Kontext keine privaten Daten liefern.

Allowlist pro Agent und Aktion, Argumentvalidierung und erforderliche Bestätigung direkt vor der Aktion prüfen. Duplikate und verspätete Ergebnisse berücksichtigen. Allgemeine Websuche standardmäßig nicht verfügbar für spezielle Geschäftsagenten.

Nachweis: fremde Firma/fremder Kunde, manipulierte Session-ID, unerlaubtes Tool, abgelaufene Bestätigung und doppelte Aktion testen. Keine Aussage, dass diese Grenzen bereits im neuen Core implementiert sind.
