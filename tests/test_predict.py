# tests/test_predict.py
import requests
import time


BASE = "http://localhost:8080"


def test_health():
    r = requests.get(f"{BASE}/health")
    assert r.status_code == 200


def test_predict_local():
    payload = {"text": "Apple announced a new product in California."}
    r = requests.post(f"{BASE}/predict", json=payload)
    assert r.status_code == 200
    j = r.json()
    assert "entities" in j
    assert "meta" in j