from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

client = TestClient(app)

# Create a new database for testing
Base.metadata.create_all(bind=engine)


# Dependency override for testing
def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides["get_db"] = override_get_db


def test_create_note():
    response = client.post(
        "/api/notes/", json={"title": "Test Note", "content": "This is a test note."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note."
    assert "id" in data


def test_read_notes():
    response = client.get("/api/notes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_note():
    # First, create a note
    response = client.post(
        "/api/notes/", json={"title": "Read Note", "content": "Content for read test."}
    )
    note_id = response.json()["id"]

    # Now, read the created note
    response = client.get(f"/api/notes/{note_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == note_id
    assert data["title"] == "Read Note"


def test_update_note():
    # Create a note
    response = client.post(
        "/api/notes/", json={"title": "Old Title", "content": "Old content."}
    )
    note_id = response.json()["id"]

    # Update the note
    response = client.put(
        f"/api/notes/{note_id}", json={"title": "New Title", "content": "New content."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["content"] == "New content."


def test_delete_note():
    # Create a note
    response = client.post(
        "/api/notes/", json={"title": "Delete Note", "content": "To be deleted."}
    )
    note_id = response.json()["id"]

    # Delete the note
    response = client.delete(f"/api/notes/{note_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == note_id

    # Ensure the note is deleted
    response = client.get(f"/api/notes/{note_id}")
    assert response.status_code == 404
