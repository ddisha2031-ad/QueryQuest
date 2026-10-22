"""CSV export helper with empty-result handling."""
from pathlib import Path
import pandas as pd

def export_csv(df, path):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    if df is None or df.empty:
        pd.DataFrame({"message":["No records match the selected filters."]}).to_csv(path,index=False)
        return path
    df.to_csv(path,index=False); return path
