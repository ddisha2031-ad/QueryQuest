import streamlit as st, plotly.express as px
f=st.session_state["filtered"]()
st.header("Customer Satisfaction")
s=f[f.satisfaction_score.notna()]
if s.empty: st.info("No satisfaction responses match the filters."); st.stop()
c1,c2=st.columns(2)
c1.metric("Average CSAT",f"{s.satisfaction_score.mean():.2f}"); c2.metric("Responses",f"{len(s):,}")
c1.plotly_chart(px.histogram(s,x="satisfaction_score",title="CSAT distribution"),use_container_width=True)
c2.plotly_chart(px.bar(s.groupby("category").satisfaction_score.mean().reset_index(),x="category",y="satisfaction_score",title="Average CSAT by category"),use_container_width=True)
st.plotly_chart(px.scatter(s.sample(min(2000,len(s))),x="resolution_minutes",y="satisfaction_score",opacity=.35,title="Resolution time vs CSAT (association, not causation)"),use_container_width=True)
st.info(f"Missing satisfaction feedback: {int(f.satisfaction_score.isna().sum()):,} tickets.")
