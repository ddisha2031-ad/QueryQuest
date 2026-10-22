"""SQLite database helpers."""
import sqlite3
from pathlib import Path

DB_PATH = Path("database/queryquest.db")

def get_connection(db_path=DB_PATH):
    db_path = Path(db_path); db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

SCHEMA = """
CREATE TABLE IF NOT EXISTS teams(team_id INTEGER PRIMARY KEY, team_name TEXT NOT NULL, department TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS agents(agent_id INTEGER PRIMARY KEY, agent_name TEXT NOT NULL, team_id INTEGER NOT NULL REFERENCES teams(team_id), experience_band TEXT, active_status TEXT);
CREATE TABLE IF NOT EXISTS customers(customer_id INTEGER PRIMARY KEY, customer_segment TEXT, region TEXT, customer_since TEXT);
CREATE TABLE IF NOT EXISTS sla_policies(policy_id INTEGER PRIMARY KEY, priority TEXT UNIQUE, target_first_response_minutes INTEGER, target_resolution_minutes INTEGER);
CREATE TABLE IF NOT EXISTS tickets(
 ticket_id TEXT PRIMARY KEY, customer_id INTEGER REFERENCES customers(customer_id), agent_id INTEGER REFERENCES agents(agent_id),
 team_id INTEGER REFERENCES teams(team_id), created_at TEXT, first_response_at TEXT, resolved_at TEXT, ticket_status TEXT,
 priority TEXT, category TEXT, subcategory TEXT, channel TEXT, policy_id INTEGER REFERENCES sla_policies(policy_id),
 satisfaction_score REAL, reopened_count INTEGER);
CREATE INDEX IF NOT EXISTS idx_tickets_created ON tickets(created_at);
CREATE INDEX IF NOT EXISTS idx_tickets_status ON tickets(ticket_status);
CREATE INDEX IF NOT EXISTS idx_tickets_priority ON tickets(priority);
CREATE INDEX IF NOT EXISTS idx_tickets_category ON tickets(category);
CREATE INDEX IF NOT EXISTS idx_tickets_channel ON tickets(channel);
CREATE INDEX IF NOT EXISTS idx_tickets_team ON tickets(team_id);
CREATE INDEX IF NOT EXISTS idx_tickets_agent ON tickets(agent_id);
"""

def load_dataframe(conn, df, table):
    df.to_sql(table, conn, if_exists="replace", index=False)

def init_schema(conn):
    conn.executescript(SCHEMA); conn.commit()
