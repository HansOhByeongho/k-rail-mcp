# K-Rail MCP

Korean railway, station and transport-data MCP research server.

> Early-stage public-sector AI research prototype. Official data, laws and statistics must be verified against their source before decision-making.

## Scope
- API-first modular architecture
- Korean public-data integration ready
- deterministic local fallback
- tests and CI-ready layout
- no API keys, personal data, internal documents or generated reports committed

## Run
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Environment
Copy `.env.example` to your local environment and provide only the credentials you actually use. Never commit credentials.

## Relationship
Designed as an independent component that can later be orchestrated by [National AI Orchestrator](https://github.com/HansOhByeongho/national-ai-orchestrator).
