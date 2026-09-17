"""In-memory data access for projects."""

from typing import Optional

from app.schemas.project import Project


class ProjectRepository:
    """Provide project data from a temporary in-memory source."""

    def __init__(self) -> None:
        self._projects = [
            Project(
                id="P001",
                name="پروژه نمونه نیروگاه",
                status="در حال اجرا",
            )
        ]

    def get_all(self) -> list[Project]:
        """Return all projects in the data source."""
        return self._projects.copy()

    def get_by_id(self, project_id: str) -> Optional[Project]:
        """Return a project matching *project_id*, if present."""
        return next((project for project in self._projects if project.id == project_id), None)
