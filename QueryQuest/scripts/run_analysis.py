"""Executes every catalogued SQL query and exports results to CSV."""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.database import get_connection

if __name__=="__main__":
    conn=get_connection()
    catalog=pd.read_csv("sql/query_catalog.csv")
    ok=0
    for _,row in catalog.iterrows():
        sql=Path(row["file"]).read_text().split("
",2)[2]
        df=pd.read_sql_query(sql,conn)
        Path("exports").mkdir(exist_ok=True)
        df.to_csv(f"exports/{row['query_id']}.csv",index=False)
        ok+=1
    print(f"Executed and exported {ok}/{len(catalog)} SQL queries.")
