# MLOps Concrete Service (FastAPI + MLflow + Prometheus + Grafana)

Production-style MLOps demo project: a containerized ML inference API for concrete compressive strength prediction, with monitoring and experiment tracking.

## Tech Stack
- **FastAPI** inference service (`/predict`, `/health`, `/metrics`)
- **MLflow** tracking UI (local)
- **Prometheus** metrics scraping
- **Grafana** dashboards (auto-provisioned)

## Architecture
Client → FastAPI (Prometheus metrics)  
Prometheus → Grafana  
FastAPI → MLflow (tracking UI)

## Quickstart (30 seconds)
Requirements: Docker + Docker Compose

```bash
make up
make load   # optional: generate traffic