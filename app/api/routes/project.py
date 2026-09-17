"""HTTP endpoints for projects."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.project import Project, ProjectListResponse
from app.services.project_service import ProjectService


router = APIRouter(prefix="/api/projects", tags=["projects"])
project_service = ProjectService()


@router.get("", response_model=ProjectListResponse)
async def list_projects() -> ProjectListResponse:
    """Return all available projects."""
    return ProjectListResponse(projects=project_service.get_projects())


@router.get("/{project_id}", response_model=Project)
async def get_project(project_id: str) -> Project:
    """Return one project or a Persian 404 response when it is absent."""
    project = project_service.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="پروژه مورد نظر یافت نشد.",
        )
    return project
