"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.routes.project import router as project_router


app = FastAPI(title="AI Project Management Assistant API")

app.include_router(project_router)


@app.get("/")
async def root() -> dict[str, str]:
    """Confirm that the API is running."""
    return {"message": "AI Project Management Assistant API is running"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "ok"}
