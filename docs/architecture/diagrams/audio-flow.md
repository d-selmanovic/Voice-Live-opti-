# audio-flow

Status: statisch aus Referenzcode abgeleitet; Core noch nicht migriert.

```mermaid
sequenceDiagram
 participant B as Browser
 participant S as App-Server
 participant L as GPT-Live
 B->>S: Session anfordern
 S->>L: Session erstellen
 S-->>B: Verbindungsantwort
 B->>L: Mikrofon über WebRTC
 L-->>B: Audio über WebRTC
 L-->>S: Gesprächs- und Tool-Ereignisse
 S->>L: Geprüfte Ergebnisse und Steuerung
```

Audioerzeugung, tatsächliches Abspielen und technische Aktionsausführung sind getrennt nachzuweisen. Quellen S03/S04/S07/S14. Keine Aussage über derzeitige Live-Verfügbarkeit.
