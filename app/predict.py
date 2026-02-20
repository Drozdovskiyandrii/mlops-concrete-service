import joblib
import pandas as pd

from app.config import MODEL_PATH, FEATURES

_model = joblib.load(MODEL_PATH)

def predict(data: dict) -> float:
    df = pd.DataFrame([data])
    df = df[FEATURES]  # enforce exact feature order
    pred = _model.predict(df)[0]
    return float(pred)
