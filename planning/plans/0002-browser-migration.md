# Browsermigration — ISS-002

Quelle: voice-agent fba6401; Ziel: strukturiertes Repository Voice-Live-opti-. Auftrag: übernehmen und lokal testen, kein Render-Deploy.

- [x] Relative Imports, Frontendpfad und private Datenpfade angepasst.
- [x] Paketabhängigkeiten und lokale Startbefehle eingerichtet.
- [x] 13 vorhandene und 2 migrationsbezogene Tests bestanden.
- [x] JavaScript-Syntax und lokale HTTP-Endpunkte geprüft.
- [x] Editable Installation mit vorhandenen Abhängigkeiten geprüft.
- [ ] Frische Mac-Installation und echter Browser-/Audiotest.

Entscheidung: funktionierende Referenzdemo als gekapselten Bereich übernehmen, bevor allgemeine Module extrahiert werden. Websuche bleibt nur im allgemeinen Demoprofil; keine neue Kundentool-Freigabe. Vorhandene aiohttp-Warnungen zu AppKey/Testzustandsänderung bleiben als technische Schuld; keine Testfehler. Browserzugriff hier gesperrt (ERR_BLOCKED_BY_CLIENT), keine Hörprüfung behaupten. Kein Cloud-Deploy.

Rücknahme: Migration per neuem Revert-Commit zurücknehmen; private lokale Daten gesondert sichern.
