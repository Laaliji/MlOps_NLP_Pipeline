from app.model import extract_entities
import time


def test_latency_small():
    texts = [
        "Apple released a new iPhone.",
        "The football match between Real Madrid and Barcelona ended 2-1.",
    ]
    latencies = []
    for t in texts:
        out = extract_entities(t)
        latencies.append(out["meta"]["latency_s"])
    avg = sum(latencies) / len(latencies)
    assert avg < 10.0  # CPU may be slow; adjust if necessary