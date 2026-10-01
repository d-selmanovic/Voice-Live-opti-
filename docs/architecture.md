# Architekturvorschlag

Browser oder spaeter Telefonie liefert Audio an die Sprachschnittstelle. Der modulare Backend-Server verwaltet Session, freigegebene Tools, Wissen, Memory und Berechtigungen. Die genaue Audioanbindung wird vor der Migration am bestehenden Code geprueft.

Externe Aufgaben nur bei Bedarf aufrufen, asynchron verarbeiten, mit Zeitlimits und klaren Rueckmeldungen. Keine zweite KI-Runde fuer jeden Smalltalk-Beitrag voraussetzen. Die konkrete Delegationsarchitektur und Modellwahl sind offen.

Memory, Wissen und Zugangsdaten liegen ausserhalb von Git. Getrennte Repositories ersetzen keine serverseitige Datentrennung. Ein Kundenprojekt legt eine gepruefte Core-Version fest.

Ein Template startet neue Projekte; es verteilt spaetere Core-Verbesserungen nicht automatisch. Diese kommen ueber kontrollierte Paketupdates.
