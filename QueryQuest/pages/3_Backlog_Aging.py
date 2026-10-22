import streamlit as st, plotly.express as px
f=st.session_state["filtered"]()
st.header("Backlog & Aging")
b=f[f.is_open]
if b.empty: st.info("No open tickets match the filters."); st.stop()
c1,c2,c3=st.columns(3)
c1.metric("Open backlog",len(b)); c2.metric("High-priority unresolved",int(b.priority.isin(["Critical","High"]).sum())); c3.metric("Oldest age (days)",f"{b.age_hours.max()/24:.1f}")
st.plotly_chart(px.histogram(b,x="age_band",title="Open tickets by age band"),use_container_width=True)
st.subheader("Longest-waiting tickets")
st.dataframe(b.nlargest(25,"age_hours")[["ticket_id","priority","category","team_id","created_at","age_hours"]])
st.download_button("Export backlog CSV",b.to_csv(index=False),"backlog.csv","text/csv")
