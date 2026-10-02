# Identitäten und Datenmodell — Entwurf

Organisation/Projekt grenzt Daten ab; agent_id bestimmt die Rolle; config_version bestimmt die gültigen Regeln. session_id bindet einen Gesprächslauf. customer_id ist nur nach serverseitig belegter Identifizierung zu verwenden. Keine Engine-ID definiert; Q02 offen.

Tool-Aufgaben benötigen operation_id, Sessionzuordnung und Revision. Ein veraltetes Ergebnis darf keine neue Aufgabe bestätigen. Idempotenz muss das Geschäftsereignis abdecken, nicht nur eine flüchtige Modell-call-ID.

Memory-Eintrag: Firmen-/Projektbezug, verifizierter Kundenbezug, Schlüssel, Wert, Herkunft, Zeit, Gültigkeit und Löschstatus. Wissensquelle: Firma, Quelle, Version, Freigabe und Aktualität. Datenbanktabellen und Migrationen erst nach Adapter-/Schemaentscheidung.
