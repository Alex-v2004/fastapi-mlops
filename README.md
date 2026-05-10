# FastAPI ML Prediction API

This project is a simple Machine Learning Prediction API built using FastAPI.

## Features

- FastAPI backend
- ML model integration
- Prediction endpoint
- Request validation using Pydantic
- Swagger API documentation

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Uvicorn
- Pydantic
- Docker
---

## Project Structure

```text
fastapi_project/
│
├── app/
│   ├── main.py
│   └── schemas.py
│
├── model/
│   └── model.pkl
│
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
├── Dockerfile
├── .dockerignore

## Docker Support

This project is fully containerized using Docker.

### Build Docker Image

```bash
docker build -t fastapi-mlops .
```

### Run Docker Container

```bash
docker run -p 8000:8000 fastapi-mlops
```

### Access API

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Docker Concepts Used

- Dockerfile
- Docker Image
- Docker Container
- Port Mapping
- Dependency Isolation