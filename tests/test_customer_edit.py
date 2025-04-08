import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_customer_edit():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/customer/edit/1")
    assert response.status_code == 200
    # Add more assertions to verify the response data

@pytest.mark.asyncio
async def test_post_customer_edit():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/customer/edit/1", data={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Customer John Doe with email john.doe@example.com updated successfully!"}
    # Add more assertions to verify the database update logic