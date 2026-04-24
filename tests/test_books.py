from httpx import AsyncClient
from main import app
import pytest

@pytest.mark.asyncio
async def test_create_and_get_book():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/books", json={
            "title": "Test",
            "author": "Me",
            "description": "desc",
            "status": "available",
            "year": 2020
        })
        assert response.status_code == 201
        data = response.json()

        book_id = data["id"]

        response = await ac.get(f"/books/{book_id}")
        assert response.status_code == 200