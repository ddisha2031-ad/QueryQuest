import streamlit as st
import pandas as pd
from src.analysis import load_tables

st.set_page_config(page_title="QueryQuest",page_icon=":bar_chart:",layout="wide")
st.title("QueryQuest — Customer Support & Operations Analytics")
st.caption("Synthetic demonstration data. All agents, customers, and tickets are fictional.")

@st.cache_resource
def tables():
    return load_tables()

t=tables()
if "filters" not in st.session_state: st.session_state.filters={}

with st.sidebar:
    st.header("Global filters")
    dates=st.date_input("Created date range",[t["tickets"].created_at.min().date(),t["tickets"].created_at.max().date()])
    st.session_state.filters["start"]=pd.Timestamp(dates[0])
    st.session_state.filters["end"]=pd.Timestamp(dates[1])+pd.Timedelta(days=1)
    for col,label in [("priority","Priority"),("ticket_status","Status"),("category","Category"),("channel","Channel")]:
        st.session_state.filters[col]=st.multiselect(label,sorted(t["tickets"][col].dropna().unique().tolist()))
    teams=st.multiselect("Team",sorted(t["teams"]["team_name"].tolist()))
    st.session_state.filters["team_id"]=t["teams"][t["teams"]["team_name"].isin(teams)]["team_id"].tolist()
    agents=st.multiselect("Agent",sorted(t["agents"]["agent_name"].tolist()))
    st.session_state.filters["agent_id"]=t["agents"][t["agents"]["agent_name"].isin(agents)]["agent_id"].tolist()

def filtered():
    d=t["tickets"]
    m=(d["created_at"]>=st.session_state.filters["start"])&(d["created_at"]<st.session_state.filters["end"])
    for col in ["priority","ticket_status","category","channel"]:
        if st.session_state.filters[col]: m&=d[col].isin(st.session_state.filters[col])
    if st.session_state.filters["team_id"]: m&=d["team_id"].isin(st.session_state.filters["team_id"])
    if st.session_state.filters["agent_id"]: m&=d["agent_id"].isin(st.session_state.filters["agent_id"])
    return d[m]

st.session_state["filtered"]=filtered
st.success("Use the sidebar filters, then open a page from the left navigation.")
