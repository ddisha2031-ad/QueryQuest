import streamlit as st, pandas as pd
st.header("Business Recommendations")
recs=[
("Critical-priority SLA compliance is lowest","Critical SLA compliance is about 50% in the priority SLA query","Critical incidents may be aging beyond contractual targets","Daily critical-backlog escalation review with ownership and due dates","Critical SLA compliance rate and overdue critical tickets","Confirm whether ticket complexity or staffing drives the gap"),
("Substantial unresolved backlog","About 3,095 open/pending tickets in the KPI summary","Customers may experience delayed resolution and repeat contacts","Implement backlog triage and aging-based escalation","Open backlog and 7+ day backlog count","Validate backlog composition by category and team"),
("Satisfaction varies by category","CSAT-by-category query shows lower scores for some categories","Process or product issues may be driving dissatisfaction","Root-cause review for the two lowest-CSAT categories","Category-level average CSAT","Correlation is not causation; collect qualitative feedback"),
]
for title,obs,imp,act,kpi,lim in recs:
    with st.expander(title):
        st.markdown(f"**Observed issue:** {obs}\n\n**Supporting metric:** {imp}\n\n**Operational implication:** {imp}\n\n**Suggested action:** {act}\n\n**KPI to monitor:** {kpi}\n\n**Limitations:** {lim}")
