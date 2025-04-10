import pytest
from fastapi.testclient import TestClient
from app.main import app
from application.dto.agents_dto import AgentsDto

client = TestClient(app)

@pytest.mark.asyncio
async def test_llm_reflect_correct_response():
    response = client.post("/llm-reflect", json={"input": "Some ambiguous request"})
    assert response.status_code == 200
    assert "Corrected response" in response.json().get("content")

@pytest.mark.asyncio
async def test_llm_reflect_incorrect_response():
    response = client.post("/llm-reflect", json={"input": "Another ambiguous request"})
    assert response.status_code == 200
    assert "Corrected response" in response.json().get("content")

@pytest.mark.asyncio
async def test_llm_reflect_no_correction():
    response = client.post("/llm-reflect", json={"input": "Clear request"})
    assert response.status_code == 200
    assert "Initial response" in response.json().get("content")
