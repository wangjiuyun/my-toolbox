from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message":"hello toolbox"}


def test_echo_empty_text_422():
    res = client.post("/echo", json={"text": ""})
    assert res.status_code == 422


def test_word_count_success():
    res = client.post("/word_count", json={"text": "hello   world"})
    assert res.status_code == 200
    assert res.json() == {
        "count": 2,
        "words": ["hello", "world"],
    }