"""Basic API integration tests."""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_projects() -> None:
    response = client.get("/api/projects")

    assert response.status_code == 200
    assert response.json() == {
        "projects": [
            {"id": "P001", "name": "پروژه نمونه نیروگاه", "status": "در حال اجرا"}
        ]
    }


def test_get_project() -> None:
    response = client.get("/api/projects/P001")

    assert response.status_code == 200
    assert response.json() == {
        "id": "P001",
        "name": "پروژه نمونه نیروگاه",
        "status": "در حال اجرا",
    }


def test_get_missing_project_returns_persian_404() -> None:
    response = client.get("/api/projects/UNKNOWN")

    assert response.status_code == 404
    assert response.json() == {"detail": "پروژه مورد نظر یافت نشد."}
