import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "concrete.csv"

def load_concrete() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. "
            "Place the CSV there as training/data/concrete.csv"
        )
    df = pd.read_csv(DATA_PATH)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df
