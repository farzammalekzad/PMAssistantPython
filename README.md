# AI Project Management Assistant

An enterprise-oriented API foundation for an AI Project Management Assistant. This initial version provides only a FastAPI service skeleton and health-check endpoint; AI, database, authentication, and external integrations will be added incrementally later.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Test the health endpoint

With the server running, visit `http://127.0.0.1:8000/health` or run:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status": "ok"}
```
