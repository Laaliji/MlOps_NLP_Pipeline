# Use official slim Python image
FROM python:3.10-slim
WORKDIR /app


# system deps for torch/transformers may be needed; keep minimal
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
&& rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .
ENV PYTHONUNBUFFERED=1
EXPOSE 8080 8000


CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]