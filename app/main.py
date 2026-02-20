from fastapi import FastAPI

app = FastAPI(title="Concrete Strength MLOps Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}
