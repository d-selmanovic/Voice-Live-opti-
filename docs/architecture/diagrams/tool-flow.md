# tool-flow

Status: geplanter Vertrag, nicht implementiert.

```mermaid
flowchart TD
 E[Tool-Anforderung] --> V{Identität und Tool erlaubt?}
 V -->|Nein| N[Ablehnen und erklären]
 V -->|Ja| C{Bestätigung und Revision gültig?}
 C -->|Nein| N
 C -->|Ja| X[Einmalig ausführen]
 X --> O{Ergebnis gültig und aktuell?}
 O -->|Nein| F[Fehler oder veraltetes Ergebnis]
 O -->|Ja| A[Erfolg bestätigen]
```

Audioerzeugung, tatsächliches Abspielen und technische Aktionsausführung sind getrennt nachzuweisen. Quellen S03/S04/S07/S14. Keine Aussage über derzeitige Live-Verfügbarkeit.
