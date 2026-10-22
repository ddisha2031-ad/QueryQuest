"""Loads database tables into analysis-ready DataFrames."""
import pandas as pd
from .database import get_connection

def load_tables(conn=None):
    if conn is None: conn=get_connection()
    tables={}
    for t in ["tickets","agents","teams","customers","sla_policies"]:
        tables[t]=pd.read_sql_query(f"SELECT * FROM {t}",conn)
    from .metrics import add_metrics
    tables["tickets"]=add_metrics(tables["tickets"])
    return tables
