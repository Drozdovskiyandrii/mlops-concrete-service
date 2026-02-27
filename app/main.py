from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from app.schemas import ConcreteInput
from app.predict import predict

app = FastAPI(title="MLOps Concrete Service", version="1.0.0")

# Expose Prometheus metrics at /metrics
Instrumentator().instrument(app).expose(app, endpoint="/metrics")


@app.get("/health")
def health() -> str:
    return "OK"


@app.post("/predict")
def predict_strength(input_data: ConcreteInput) -> dict:
    try:
        out = predict(input_data.model_dump())

        # ✅ normalize output (some versions may return float)
        if isinstance(out, (int, float)):
            return {"predicted_strength_mpa": float(out)}
        if isinstance(out, dict):
            return out

        raise HTTPException(status_code=500, detail=f"Unexpected predict() return type: {type(out)}")

    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Model artifact not found: {e}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e