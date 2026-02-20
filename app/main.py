from fastapi import FastAPI
from starlette.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from app.schemas import ConcreteInput
from app.predict import predict
from app.config import FEATURES, MODEL_PATH
from app.metrics import PrometheusMiddleware

app = FastAPI(title="Concrete Strength MLOps Service")

# Prometheus metrics middleware
app.add_middleware(PrometheusMiddleware)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/model-info")
def model_info():
    return {
        "model_path": str(MODEL_PATH),
        "features": FEATURES,
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/predict")
def predict_strength(input_data: ConcreteInput):
    result = predict(input_data.model_dump())
    return {"predicted_strength_mpa": result}
