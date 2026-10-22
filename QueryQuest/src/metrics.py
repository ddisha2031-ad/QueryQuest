"""Shared KPI calculations used by the dashboard and reports."""
import pandas as pd

AS_OF = pd.Timestamp("2026-10-22 18:00:00")

def add_metrics(df):
    df = df.copy()
    for c in ["created_at","first_response_at","resolved_at"]:
        df[c]=pd.to_datetime(df[c],errors="coerce")
    df["response_minutes"]=(df["first_response_at"]-df["created_at"]).dt.total_seconds()/60
    df["resolution_minutes"]=(df["resolved_at"]-df["created_at"]).dt.total_seconds()/60
    df["age_hours"]=np.where(df["resolved_at"].isna(),(AS_OF-df["created_at"]).dt.total_seconds()/3600,pd.NA) if False else (AS_OF-df["created_at"]).dt.total_seconds()/3600
    df["is_open"]=df["ticket_status"].isin(["Open","Pending"])
    df["age_band"]=pd.cut(df["age_hours"],[-1,24,72,168,720,1e9],labels=["0-24 hours","1-3 days","3-7 days","7-30 days","30+ days"])
    return df

import numpy as np
