# Versionen und Releases

0.0.0 bedeutet Grundgerüst ohne lauffähigen Voice-Agenten. Kunden-Template hat bewusst noch keine erfundene Core-Abhängigkeit. Erst geprüftes Paket veröffentlichen, Bezugsquelle dokumentieren und konkrete Version eintragen.

Vor Release: Wheel-Installation in frischer Umgebung, passende Tests, Lizenzentscheidung, dokumentierter Rollback. Neue Abhängigkeiten mit begründeten Versionen und reproduzierbarem Lock-Verfahren festlegen, sobald der Runtime-Stack gewählt ist. Jetzt gibt es keine Runtime-Abhängigkeiten zu locken.

CI-Actions sind zunächst mit Major-Tags beschrieben; vor externer Aktivierung auf geprüfte Commit-SHAs festlegen. Workflow wurde lokal geprüft, nicht auf GitHub ausgeführt.
