import sys
from pathlib import Path
import pandas as pd, pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.data_generator import generate
from src.data_cleaning import clean_tickets

@pytest.fixture(scope="session")
def raw():
    return generate("data/raw")

@pytest.fixture(scope="session")
def clean(raw):
    df,log=clean_tickets(raw)
    return df,log
