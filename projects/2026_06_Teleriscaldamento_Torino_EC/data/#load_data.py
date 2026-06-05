# load_data.py
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
RAW = ROOT / "data" / "raw" / "2026"

def carica_dati(fonte: str, file: str) -> pd.DataFrame:
    percorso = RAW / fonte / file
    return pd.read_csv(percorso)
