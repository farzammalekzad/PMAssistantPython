# AI Project Management Assistant

The Step 2 API foundation for an AI Project Management Assistant. This version deliberately uses only in-memory project data. It does not yet include SQL Server, LLMs, RAG, agents, or authentication.

## Architecture

Requests use a clear layered flow:

```text
Request -> API Router -> Service -> Repository -> In-memory data source
```

- `app/api/routes/` contains HTTP routes and HTTP-specific errors.
- `app/services/` contains project use-case/business logic.
- `app/repositories/` reads project data; it currently uses a mock in-memory list.
- `app/schemas/` contains Pydantic models that define API data.

## Setup and run

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/` | API status message |
| GET | `/health` | Health check |
| GET | `/api/projects` | List projects |
| GET | `/api/projects/{project_id}` | Get one project |

Examples:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/api/projects
curl http://127.0.0.1:8000/api/projects/P001
```

The project list response is:

```json
{
  "projects": [
    {
      "id": "P001",
      "name": "پروژه نمونه نیروگاه",
      "status": "در حال اجرا"
    }
  ]
}
```

An unknown project returns HTTP 404 with a Persian error message.

## Tests

Run the tests with:

```bash
pytest
```
