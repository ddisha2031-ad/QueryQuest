"""Loads cleaned CSV data into SQLite."""
import pandas as pd
from pathlib import Path
from .database import get_connection, init_schema, load_dataframe

def load_database(raw_dir="data/raw", processed_dir="data/processed", db_path="database/queryquest.db"):
    from .data_cleaning import clean_tickets
    raw, proc = Path(raw_dir), Path(processed_dir); proc.mkdir(parents=True, exist_ok=True)
    tickets = pd.read_csv(raw/"tickets_raw.csv", parse_dates=["created_at","first_response_at","resolved_at"])
    tickets, log = clean_tickets(tickets)
    tickets.to_csv(proc/"tickets_clean.csv", index=False)
    conn = get_connection(db_path); init_schema(conn)
    load_dataframe(conn, pd.read_csv(raw/"teams.csv"), "teams")
    load_dataframe(conn, pd.read_csv(raw/"agents.csv"), "agents")
    load_dataframe(conn, pd.read_csv(raw/"customers.csv"), "customers")
    load_dataframe(conn, pd.read_csv(raw/"sla_policies.csv"), "sla_policies")
    t = tickets.copy()
    for c in ["created_at","first_response_at","resolved_at"]:
        t[c]=pd.to_datetime(t[c]).dt.strftime("%Y-%m-%d %H:%M:%S")
    load_dataframe(conn, t, "tickets")
    conn.commit()
    return conn, log
