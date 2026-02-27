from pathlib import Path
import joblib
import numpy as np
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

from training.data import load_concrete

ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "model.joblib"

def main():
    print("TRAIN SCRIPT STARTED")
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    df = load_concrete()
    target = "strength"

    X = df.drop(columns=[target])
    y = df[target]

    split_params = {
        "test_size": 0.2,
        "random_state": 42
    }

    model_params = {
        "n_estimators": 400,
        "random_state": 42,
        "n_jobs": -1
    }

    mlflow.set_experiment("concrete-strength-mlops")

    with mlflow.start_run():
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, **split_params
        )

        model = RandomForestRegressor(**model_params)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        rmse = float(np.sqrt(mean_squared_error(y_test, preds)))
        r2 = float(r2_score(y_test, preds))

        # Log params
        mlflow.log_params(model_params)
        mlflow.log_params(split_params)

        # Log metrics
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)

        # Log model
        mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="concrete_strength_model")

        joblib.dump(model, MODEL_PATH)

        run_id = mlflow.active_run().info.run_id
        print(f"MLflow run_id: {run_id}")
        print(f"Saved model to: {MODEL_PATH}")
        print(f"RMSE: {rmse:.3f}")
        print(f"R2:   {r2:.3f}")

if __name__ == "__main__":
    main()
