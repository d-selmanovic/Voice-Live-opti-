# system

Status: statisch aus Referenzcode abgeleitet; Core noch nicht migriert.

```mermaid
flowchart TD
 B[Browser] <-->|Audio via WebRTC| L[GPT-Live]
 B <-->|Login und Status| S[App-Server]
 S <-->|Steuerung via Sideband| L
 L <-->|Delegation| R[Responses-Backend]
 S --> T[Tool-Executor]
 T --> D[Freigegebene Dienste]
```

Audioerzeugung, tatsächliches Abspielen und technische Aktionsausführung sind getrennt nachzuweisen. Quellen S03/S04/S07/S14. Keine Aussage über derzeitige Live-Verfügbarkeit.
