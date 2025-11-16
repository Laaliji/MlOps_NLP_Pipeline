from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import extract_entities, health_check
import logging
from prometheus_client import start_http_server, Summary, Counter


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nlp_api")


# Prometheus metrics (start a small metrics server on port 8000)
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency')
REQUEST_COUNT = Counter('request_count', 'Total request count')


# start prometheus metrics server (non-blocking)
try:
    start_http_server(8000)
    logger.info("Prometheus metrics available on :8000")
except Exception:
    logger.warning("Could not start Prometheus server (already running?)")


app = FastAPI()


class TextIn(BaseModel):
    text: str


@app.get("/health")
def health():
    return health_check()


@app.post("/predict")
@REQUEST_LATENCY.time()
def predict(payload: TextIn):
    REQUEST_COUNT.inc()
    logger.info(f"request_chars={len(payload.text)}")
    try:
        result = extract_entities(payload.text)
        return result
    except Exception as e:
        logger.exception("Predict error")
        raise HTTPException(status_code=500, detail=str(e))


# helpful when running locally: uvicorn app.app:app --host 0.0.0.0 --port 8080