"""Pydantic schemas used by the project API."""

from pydantic import BaseModel


class Project(BaseModel):
    """A project returned by the API."""

    id: str
    name: str
    status: str


class ProjectListResponse(BaseModel):
    """The response body for the project collection endpoint."""

    projects: list[Project]
