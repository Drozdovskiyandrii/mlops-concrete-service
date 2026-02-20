# MLOps Concrete Service

Production-style MLOps project: train + track (MLflow) + serve (FastAPI) + containerize + deploy.

## MLflow Registry (Serving)
- Train + register model: `python -m training.train`
- Set Production alias in MLflow UI: `concrete_strength_model` -> alias `Production`
- Run API with registry:
  - `mlflow ui --host 127.0.0.1 --port 5000`
  - `MLFLOW_TRACKING_URI=http://127.0.0.1:5000 uvicorn app.main:app --reload`
