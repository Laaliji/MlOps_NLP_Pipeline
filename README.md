# mlops-nlp-pipeline-demo

End-to-end, free MLOps demo for NLP: FastAPI model, Docker, CI (GitHub Actions), tests, and Hugging Face Spaces deploy template. Perfect for practicing and showing on a CV.

## Features

- FastAPI inference service (entity extraction + simple categorization)
- Dockerfile for local & cloud deploy
- GitHub Actions: run tests on push
- Tests with pytest and sample testset
- Optional Hugging Face Spaces Docker template
- Prometheus metrics stub

## Quickstart (local)

1. Clone repo

```bash
git clone https://github.com/Laaliji/MlOps_NLP_Pipeline.git
cd MlOps_NLP_Pipeline
```

2. Build and run locally

```bash
docker build -t nlp-model:dev .
docker run -p 8080:8080 nlp-model:dev
```

3. Health check

```bash
curl http://localhost:8080/health
```

4. Predict

```bash
curl -s -X POST "http://localhost:8080/predict" -H "Content-Type: application/json" -d '{"text":"Apple released a new iPhone."}' | jq
```
