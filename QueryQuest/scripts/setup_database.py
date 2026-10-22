"""Rebuilds the SQLite database from raw/generated data."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.data_generator import generate
from src.data_loader import load_database

if __name__=="__main__":
    generate("data/raw")
    conn, log = load_database()
    print("Database rebuilt: database/queryquest.db")
    for item in log: print(" -",item)
