# MLOps NLP Pipeline Demo

Complete end-to-end MLOps pipeline for NLP: FastAPI model serving, Docker containerization, CI/CD with GitHub Actions, automated testing, and monitoring. Perfect for demonstrating MLOps skills on your CV.

## 🚀 Features

- **Model Serving**: FastAPI service with BERT-based Named Entity Recognition
- **Smart Categorization**: Automatic content classification (news/other)
- **Containerization**: Docker setup for consistent deployment
- **CI/CD Pipeline**: GitHub Actions for automated testing
- **Monitoring**: Prometheus metrics for latency and request tracking
- **Testing Suite**: Unit tests for model performance and API endpoints
- **Production Ready**: Hugging Face Spaces deployment template

## 🏗️ Architecture

```
├── app/                    # FastAPI application
│   ├── app.py             # Main API endpoints
│   ├── model.py           # BERT NER model logic
│   └── preprocessing.py   # Text preprocessing utilities
├── tests/                 # Test suite
├── infra/                 # Infrastructure & deployment
├── .github/workflows/     # CI/CD pipelines
└── requirements.txt       # Dependencies
```

## 🚀 Quick Start

### Option 1: Python Development (Recommended for development)

1. **Clone and setup**

```bash
git clone https://github.com/Laaliji/MlOps_NLP_Pipeline.git
cd MlOps_NLP_Pipeline
pip install -r requirements.txt
```

2. **Run the server**

```bash
python -m uvicorn app.app:app --host 0.0.0.0 --port 8080 --reload
```

3. **Test the API**

```bash
# Health check
curl http://localhost:8080/health

# Entity extraction
curl -X POST "http://localhost:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"Apple released a new iPhone in California."}'
```

### Option 2: Docker (Production-like)

1. **Build and run**

```bash
docker build -t nlp-model:dev .
docker run -p 8080:8080 -p 8000:8000 nlp-model:dev
```

2. **Test endpoints**

```bash
# Health check
curl http://localhost:8080/health

# Prediction with JSON formatting
curl -s -X POST "http://localhost:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"Microsoft announced new Azure features."}' | jq
```

## 🧪 Testing

Run the complete test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific tests
python -m pytest tests/test_latency.py -v
```

## 📊 Monitoring

- **API Metrics**: Available at `http://localhost:8000/metrics` (Prometheus format)
- **Health Check**: `GET /health`
- **Request Latency**: Automatically tracked per prediction
- **Request Count**: Total API calls counter

## 🔄 MLOps Workflow

### 1. Development Phase

- Develop and test locally using Python
- Run unit tests: `python -m pytest tests/ -v`
- Test API endpoints manually

### 2. Integration Phase

- Push code to GitHub
- GitHub Actions automatically runs tests
- Docker image builds and validates

### 3. Deployment Phase

- Deploy to staging/production
- Monitor with Prometheus metrics
- Scale based on usage patterns

### 4. Monitoring & Maintenance

- Track model performance
- Monitor API latency and errors
- Update model versions as needed

## 🛠️ MLOps Process Explained

### What is MLOps?

MLOps (Machine Learning Operations) is the practice of applying DevOps principles to ML systems. It covers the entire ML lifecycle from development to production.

### This Project's MLOps Components:

#### 1. **Model Development & Versioning**

- **Model**: BERT-based NER (`dslim/bert-base-NER`)
- **Framework**: Hugging Face Transformers with PyTorch
- **Versioning**: Model weights automatically downloaded and cached

#### 2. **API Development**

- **Framework**: FastAPI for high-performance API serving
- **Validation**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive exception handling and logging

#### 3. **Testing Strategy**

- **Unit Tests**: Model performance and latency testing
- **Integration Tests**: API endpoint testing
- **Automated Testing**: GitHub Actions runs tests on every push

#### 4. **Containerization**

- **Docker**: Consistent environment across dev/staging/prod
- **Multi-stage builds**: Optimized for production deployment
- **Port mapping**: API (8080) and metrics (8000)

#### 5. **CI/CD Pipeline**

```yaml
# .github/workflows/tests.yml
Push to GitHub → Run Tests → Build Docker → Deploy (if tests pass)
```

#### 6. **Monitoring & Observability**

- **Prometheus Metrics**: Request latency, count, errors
- **Logging**: Structured logging with request details
- **Health Checks**: Endpoint for service monitoring

#### 7. **Deployment Options**

- **Local**: Development and testing
- **Docker**: Production-ready containerized deployment
- **Hugging Face Spaces**: Free cloud hosting for demos
- **Cloud**: AWS, GCP, Azure (using provided Docker image)

## 🚀 Launching the Complete MLOps Process

### Step 1: Local Development

```bash
# Start development server
python -m uvicorn app.app:app --host 0.0.0.0 --port 8080 --reload

# In another terminal, run tests
python -m pytest tests/ -v
```

### Step 2: Trigger CI/CD Pipeline

```bash
# Commit your changes
git add .
git commit -m "feat: update model or add feature"
git push origin main

# This triggers:
# 1. GitHub Actions workflow
# 2. Automated testing
# 3. Docker build validation
```

### Step 3: Monitor the Pipeline

- Check GitHub Actions tab for build status
- Review test results and logs
- Verify Docker image builds successfully

### Step 4: Production Deployment

```bash
# Option A: Docker deployment
docker build -t nlp-model:prod .
docker run -d -p 8080:8080 -p 8000:8000 --name nlp-api nlp-model:prod

# Option B: Cloud deployment (example with Docker)
# Push to container registry and deploy to your cloud provider
```

### Step 5: Production Monitoring

```bash
# Check health
curl http://your-domain:8080/health

# Monitor metrics
curl http://your-domain:8000/metrics

# Test predictions
curl -X POST "http://your-domain:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"Your test text here"}'
```

## 📈 Model Performance

The current model provides:

- **Entity Types**: Organizations (ORG), Locations (LOC), Miscellaneous (MISC), Persons (PER)
- **Accuracy**: High accuracy on standard NER benchmarks
- **Latency**: ~50-200ms per request (CPU), ~10-50ms (GPU)
- **Categories**: Automatic classification as "news" or "other"

## 🔧 Customization

### Adding New Models

1. Update `app/model.py` with your model
2. Modify the `extract_entities()` function
3. Update tests in `tests/`
4. Test locally before pushing

### Scaling Considerations

- **Horizontal**: Multiple container instances behind load balancer
- **Vertical**: Increase container resources (CPU/RAM)
- **GPU**: Add GPU support for faster inference
- **Caching**: Add Redis for frequently requested predictions
