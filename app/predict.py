import os
import threading
import joblib
import pandas as pd

MODEL_PATH = os.getenv("MODEL_PATH", "/app/artifacts/model.joblib")

_model = None
_lock = threading.Lock()

def _get_model():
    global _model
    if _model is None:
        with _lock:
            if _model is None:
                _model = joblib.load(MODEL_PATH)
    return _model

def predict(features: dict) -> dict:
    model = _get_model()
    df = pd.DataFrame([features])
    y = float(model.predict(df)[0])
    return {"predicted_strength_mpa": y}