from pathlib import Path
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

from training.data import load_concrete

ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "model.joblib"

def find_target_column(cols):
    # common variants
    candidates = {
        "concrete_compressive_strength",
        "compressive_strength",
        "strength",
        "cs_mpa",
        "concrete_compressive_strength_mpa"
    }
    for c in cols:
        if c in candidates:
            return c
    # fuzzy fallback
    for c in cols:
        if "strength" in c and "compressive" in c:
            return c
    for c in cols:
        if "strength" in c:
            return c
    raise ValueError(f"Could not identify target column. Columns: {sorted(list(cols))}")

def main():
    print("TRAIN SCRIPT STARTED")

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    df = load_concrete()
    target = find_target_column(set(df.columns))

    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=400,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = float(np.sqrt(mean_squared_error(y_test, preds)))
    r2 = float(r2_score(y_test, preds))

    joblib.dump(model, MODEL_PATH)

    print(f"Saved model to: {MODEL_PATH}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R2:   {r2:.3f}")

if __name__ == "__main__":
    main()
