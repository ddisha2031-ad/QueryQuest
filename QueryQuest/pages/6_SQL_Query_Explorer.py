import streamlit as st, pandas as pd
from pathlib import Path
from src.database import get_connection
st.header("SQL Query Explorer")
st.caption("Only predefined, reviewed, read-only queries can be executed.")
catalog=pd.read_csv("sql/query_catalog.csv")
qid=st.selectbox("Select query",catalog.query_id+" — "+catalog.business_question)
row=catalog[catalog.query_id==qid.split(" — ")[0]].iloc[0]
sql=Path(row.file).read_text()
st.code(sql,language="sql")
if st.button("Run query"):
    try:
        df=pd.read_sql_query(sql,get_connection())
        st.dataframe(df.head(500))
        st.download_button("Export results CSV",df.to_csv(index=False),f"{row.query_id}.csv","text/csv")
    except Exception as e: st.error(f"Query failed: {e}")
