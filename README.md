# MLOps Concrete Strength Prediction Service

Production-ready MLOps service for predicting concrete compressive strength using a trained ML model, served via FastAPI, containerized with Docker, monitored with Prometheus + Grafana, and validated via CI pipeline.

---

## 🔍 Overview

This project demonstrates a full end-to-end MLOps workflow:

- Model training
- Artifact packaging
- Production API serving
- Docker containerization
- Monitoring with Prometheus
- Visualization with Grafana
- Load testing
- CI pipeline with GitHub Actions

The service predicts concrete compressive strength (MPa) based on material composition and curing age.

---

## 🏗 Architecture

Client → FastAPI → ML Model  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Prometheus ← /metrics endpoint  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Grafana Dashboard  

All services run via Docker Compose.

---

## 🧠 Model

- Regression model trained using scikit-learn
- Automatically trained during Docker image build
- Stored as artifact inside container
- Served via `/predict` endpoint

---

## 📦 Tech Stack

- Python 3.11
- FastAPI
- scikit-learn
- MLflow (tracking UI)
- Docker
- Docker Compose
- Prometheus
- Grafana
- GitHub Actions (CI)

---

## 🚀 Quick Start (30 seconds)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mlops-concrete-service.git
cd mlops-concrete-service