"""Documented cleaning rules. Raw data is never modified in place."""
import pandas as pd

CHANNEL_MAP = {"email":"Email","web portal":"Web Portal","live chat":"Live Chat","phone":"Phone"}
VALID_STATUS = {"Resolved","Closed","Open","Pending"}
VALID_PRIORITY = {"Critical","High","Medium","Low"}

def clean_tickets(df, cleaning_log=None):
    log = cleaning_log if cleaning_log is not None else []
    df = df.copy()
    n0 = len(df)
    df = df.drop_duplicates(subset="ticket_id", keep="first")
    log.append(f"Removed {n0-len(df)} duplicate ticket_id rows (kept first occurrence).")
    before = df["channel"].copy()
    df["channel"] = df["channel"].astype(str).str.strip().str.lower().map(CHANNEL_MAP).fillna(df["channel"])
    log.append(f"Normalized {int((before!=df['channel']).sum())} inconsistent channel labels.")
    bad_ts = df["resolved_at"].notna() & (df["resolved_at"] < df["created_at"])
    df.loc[bad_ts,"resolved_at"] = pd.NaT
    df.loc[bad_ts & df["ticket_status"].isin(["Resolved","Closed"]),"ticket_status"]="Open"
    log.append(f"Set {int(bad_ts.sum())} resolution timestamps earlier than creation to NULL and reclassified those tickets as Open.")
    bad_fr = df["first_response_at"].notna() & (df["first_response_at"] < df["created_at"])
    df.loc[bad_fr,"first_response_at"]=pd.NaT
    log.append(f"Set {int(bad_fr.sum())} first-response timestamps earlier than creation to NULL.")
    unresolved = df["ticket_status"].isin(["Open","Pending"])
    silently_resolved = unresolved & df["resolved_at"].notna()
    df.loc[silently_resolved,"resolved_at"]=pd.NaT
    log.append(f"Removed resolution timestamps from {int(silently_resolved.sum())} unresolved tickets.")
    df["satisfaction_score"]=pd.to_numeric(df["satisfaction_score"],errors="coerce")
    df["reopened_count"]=pd.to_numeric(df["reopened_count"],errors="coerce").fillna(0).astype(int)
    log.append(f"Missing satisfaction scores retained as NULL: {int(df['satisfaction_score'].isna().sum())} tickets (not imputed).")
    return df, log
