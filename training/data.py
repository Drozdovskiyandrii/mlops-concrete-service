import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "concrete.csv"

COLUMN_MAP = {
    "cement_(component_1)(kg_in_a_m^3_mixture)": "cement",
    "blast_furnace_slag_(component_2)(kg_in_a_m^3_mixture)": "blast_furnace_slag",
    "fly_ash_(component_3)(kg_in_a_m^3_mixture)": "fly_ash",
    "water_(component_4)(kg_in_a_m^3_mixture)": "water",
    "water__(component_4)(kg_in_a_m^3_mixture)": "water",
    "superplasticizer_(component_5)(kg_in_a_m^3_mixture)": "superplasticizer",
    "coarse_aggregate__(component_6)(kg_in_a_m^3_mixture)": "coarse_aggregate",
    "fine_aggregate_(component_7)(kg_in_a_m^3_mixture)": "fine_aggregate",
    "age_(day)": "age",
    "concrete_compressive_strength(mpa,megapascals)": "strength",
    "concrete_compressive_strength(mpa,_megapascals)": "strength",
    "concrete_compressive_strength_(mpa,_megapascals)": "strength",
    "concrete_compressive_strength_(mpa)": "strength",
    "concrete_compressive_strength": "strength",
}

def load_concrete() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    df = df.rename(columns={k: v for k, v in COLUMN_MAP.items() if k in df.columns})

    required = [
        "cement",
        "blast_furnace_slag",
        "fly_ash",
        "water",
        "superplasticizer",
        "coarse_aggregate",
        "fine_aggregate",
        "age",
        "strength",
    ]

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns after renaming: {missing}. "
            f"Got columns: {df.columns.tolist()}"
        )

    return df[required]
