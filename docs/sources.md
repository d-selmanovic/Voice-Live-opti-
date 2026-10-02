# Quellenregister

Geprüft am 02.10.2026. Offizielle Dokumentation unterstützt Prinzipien, nicht unsere konkreten Ordnernamen. S02 ist ausdrücklich archiviert. Keine pauschale Behauptung, alle Cookbooks geprüft zu haben.

- **S01** [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): Entwicklungsanweisungen werden hierarchisch entdeckt; Zusatzdateien ausdrücklich referenzieren. Grenze: aktuelle Dokumentation.
- **S02** [OpenAI Cookbook: PLANS.md](https://developers.openai.com/cookbook/articles/codex_exec_plans): Lebende Pläne für große Änderungen; Fortschritt, Entscheidungen, Erkenntnisse und Abnahme. Grenze: archiviertes Beispiel; nur Planungsmuster, keine Modell-/API-Empfehlung.
- **S03** [OpenAI: GPT-Live Delegation](https://developers.openai.com/api/docs/guides/live-delegation): Responses für einfachen Einstieg; Client Delegation für eigene Workflows und Ergebnisprüfung. Grenze: aktuelle Dokumentation.
- **S04** [OpenAI: Server controls](https://developers.openai.com/api/docs/guides/voice-server-controls): Audio- und Steuerverbindung unterscheiden; eine zuständige Stelle je Aktion; laufende Kontrollen. Grenze: aktuelle Dokumentation.
- **S05** [OpenAI Cookbook: GPT-Live Evaluation](https://developers.openai.com/cookbook/examples/audio/voice_agent_evaluation): Sprachverhalten, Delegation, Tools und Endzustand gemeinsam messen; schrittweise Szenarien. Grenze: Cookbook, GPT-Live-spezifisch.
- **S06** [OpenAI Cookbook: Kunden-Memory](https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization): Gezielte Erinnerungen, Zusammenführung, Konfliktlösung und Vergessen. Grenze: SDK-Beispiel, kein automatisch verfügbarer Dienst.
- **S07** [OpenAI: Guardrails](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals): Aktionsprüfungen an Tool-Grenzen; Agentenprüfungen decken nicht jede Grenze ab. Grenze: SDK-spezifisch; Prinzip auf eigene Executor-Implementierung übertragen.
- **S08** [OpenAI: Observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability): SDK-Traces zeigen Modell- und Tool-Aufrufe; SDK-Verwendung vorausgesetzt. Grenze: SDK-spezifisch.
- **S09** [OpenAI: Production](https://developers.openai.com/api/docs/guides/production-best-practices): Produktionsbetrieb gesondert planen; Zugang, Skalierung und Betrieb berücksichtigen. Grenze: keine Garantie durch Ordnernamen.
- **S10** [Python Packaging: src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/): Paketcode von Repositorydateien trennen; Installation gesondert prüfen. Grenze: Python Packaging Authority.
- **S11** [Python Packaging: pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/): Paketmetadaten und Build-Konfiguration zentral beschreiben. Grenze: Python Packaging Authority.
- **S12** [GitHub: Planung und Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/planning-and-tracking-work-for-your-team-or-project): Issues, Vorlagen und Aufgabenzerlegung werden dokumentiert. Grenze: GitHub; keine Pflicht zur sofortigen Cloud-Nutzung.
- **S13** [OpenAI: GPT-Live Prompting](https://developers.openai.com/api/docs/guides/live-prompting): Kurze Gesprächsanweisungen; ausführliche Arbeitsabläufe im Backend. Grenze: aktuelle Dokumentation.
- **S14** [OpenAI: Session Lifecycle](https://developers.openai.com/api/docs/guides/live-conversations): Transkript, Audiowiedergabe und Backendfortschritt getrennt verfolgen. Grenze: aktuelle Dokumentation.
- **S15** [OpenAI Cookbook: Session Memory](https://developers.openai.com/cookbook/examples/agents_sdk/session_memory): Gesprächshistorie und Kontextmanagement; SDK-Nutzung erforderlich. Grenze: nicht gleich dauerhafte Kunden-Memory.
- **S16** [OpenAI: Function Calling](https://developers.openai.com/api/docs/guides/function-calling): Tool-Aufrufe haben definierte Eingaben; Anwendung führt sie aus. Grenze: Berechtigungen zusätzlich serverseitig.
- **S17** [OpenMined: Syft Hub](https://syft-protocol.openmined.org/syft-sdk/): Dezentrale Datenabfragen und föderierte Pipelines. Grenze: nicht im Referenzcode integriert; keine Strukturvorgabe für unseren Core.

Maschinenlesbare Zuordnung: [sources.json](references/sources.json). OpenAI-Plugin-Installationsstatus ist hier nicht erneut nachgewiesen; Seiten wurden direkt gelesen.
