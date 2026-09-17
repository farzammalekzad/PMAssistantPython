"""Business logic for projects."""

from typing import Optional

from app.repositories.project_repository import ProjectRepository
from app.schemas.project import Project


class ProjectService:
    """Coordinate project use cases independently of HTTP and storage details."""

    def __init__(self, repository: Optional[ProjectRepository] = None) -> None:
        self._repository = repository or ProjectRepository()

    def get_projects(self) -> list[Project]:
        """Get all projects."""
        return self._repository.get_all()

    def get_project_by_id(self, project_id: str) -> Optional[Project]:
        """Get a project by its identifier."""
        return self._repository.get_by_id(project_id)
