# Sicherung und Wiederherstellung — Gültigkeitsgrenzen

Git/ZIP sichert Projektdateien, nicht Runtime-Daten, Secrets oder Kalender-/CRM-Zustände. Vor Pilot getrennte Sicherung für Datenbank/Knowledge und sichere Secret-Wiederbereitstellung definieren.

Restore zunächst in isolierter Umgebung mit synthetischen Daten: Datenversion und Appversion vergleichen, Zugriffsgrenzen prüfen, Memory-Löschregeln berücksichtigen und Ergebnis nachweisen. Konkreter Backup-/Restore-Befehl erst nach Speicherentscheidung. Der neue Core besitzt noch keinen Datenbankdienst.
