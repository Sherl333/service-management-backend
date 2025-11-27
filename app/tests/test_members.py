from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_members():
    res = client.get("/members/search?q=test")
    assert res.status_code == 200

def test_filter_members():
    res = client.get("/members/filter?status=active")
    assert res.status_code == 200
