# data-isolation

Status: geplanter Vertrag, nicht implementiert.

```mermaid
flowchart TD
 R[Anforderung] --> I[Serverseitiger Identitätskontext]
 I --> P{Projekt und Kunde erlaubt?}
 P -->|Nein| N[Zugriff ablehnen]
 P -->|Ja| M[Kundenspezifische Memory]
 P -->|Ja| K[Freigegebenes Firmenwissen]
 M --> C[Nur relevanten Kontext bereitstellen]
 K --> C
```

Audioerzeugung, tatsächliches Abspielen und technische Aktionsausführung sind getrennt nachzuweisen. Quellen S03/S04/S07/S14. Keine Aussage über derzeitige Live-Verfügbarkeit.
