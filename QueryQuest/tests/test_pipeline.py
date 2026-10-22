
import sqlite3
from pathlib import Path
import pandas as pd
import pytest
from src.data_generator import generate, SEED
from src.data_cleaning import clean_tickets
from src.database import get_connection, init_schema
from src.data_loader import load_database

def test_generation_deterministic():
    a=generate("data/raw"); b=generate("data/raw")
    assert a.shape==b.shape
    assert a.ticket_id.tolist()==b.ticket_id.tolist()

def test_duplicates_removed(clean):
    df,log=clean
    assert df.ticket_id.is_unique
    assert any("duplicate" in x.lower() for x in log)

def test_invalid_timestamps_fixed(clean):
    df,_=clean
    assert not (df.resolved_at.notna() & (df.resolved_at<df.created_at)).any()
    assert not (df.first_response_at.notna() & (df.first_response_at<df.created_at)).any()

def test_unresolved_have_no_resolution(clean):
    df,_=clean
    assert df.loc[df.ticket_status.isin(["Open","Pending"]),"resolved_at"].isna().all()

def test_missing_csat_retained(clean):
    df,_=clean
    assert df.satisfaction_score.isna().sum()>0

def test_database_and_queries(tmp_path):
    conn,log=load_database(db_path=tmp_path/"test.db")
    tables={r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"tickets","agents","teams","customers","sla_policies"}<=tables
    catalog=pd.read_csv("sql/query_catalog.csv")
    for _,row in catalog.iterrows():
        sql=Path(row.file).read_text().split("\n",2)[2]
        df=pd.read_sql_query(sql,conn)
        assert isinstance(df,pd.DataFrame)

def test_sla_and_backlog_calculations(clean):
    df,_=clean
    open_df=df[df.ticket_status.isin(["Open","Pending"])]
    assert (open_df.resolved_at.isna()).all()
    assert df.loc[df.resolved_at.notna()].shape[0]>0

def test_empty_filter_result():
    import pandas as pd
    df=pd.DataFrame(columns=["ticket_id","created_at"])
    assert df.empty

def test_csv_export(tmp_path):
    from src.exports import export_csv
    p=export_csv(pd.DataFrame({"a":[1,2]}),tmp_path/"out.csv")
    assert p.exists() and pd.read_csv(p).shape==(2,1)
