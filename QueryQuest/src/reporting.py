"""Builds the Markdown business report from executed SQL outputs."""
from pathlib import Path
import pandas as pd

def build_report(exports_dir="exports", out="reports/business_report.md"):
    e=Path(exports_dir)
    def rd(n): return pd.read_csv(e/f"{n}.csv")
    kpi=rd("34_operational_kpi_summary").iloc[0]
    sla=rd("11_sla_compliance_by_priority")
    age=rd("14_open_tickets_by_age_band")
    cat=rd("17_csat_by_category")
    lines=[]
    lines.append("# QueryQuest Business Report")
    lines.append("## Executive summary")
    lines.append(f"As of the reporting timestamp, the support organization handled **{int(kpi.total_tickets):,} tickets**, with **{int(kpi.open_backlog):,} open or pending tickets**, **{int(kpi.resolved_tickets):,} resolved tickets**, an average resolution time of **{kpi.avg_resolution_minutes:.0f} minutes**, and average customer satisfaction of **{kpi.avg_csat:.2f} / 5**.")
    lines.append("## SLA performance")
    lines.append(f"Critical tickets have the lowest compliance rate at **{sla.iloc[0].sla_compliance_rate:.1f}%**, with {int(sla.iloc[0].overdue_open)} critical tickets unresolved beyond target.")
    lines.append(sla.to_markdown(index=False))
    lines.append("## Backlog aging")
    lines.append(age.to_markdown(index=False))
    lines.append("## Customer satisfaction")
    lines.append("Lowest-satisfaction categories:")
    lines.append(cat.sort_values('avg_csat').head(3).to_markdown(index=False))
    lines.append("## Recommended actions")
    lines.append("1. Prioritize the Critical and High-priority overdue backlog through a daily escalation review.")
    lines.append("2. Investigate the lowest-SLA categories and teams; validate whether staffing, routing, or ticket complexity drives delays.")
    lines.append("3. Review first-response workflows for tickets waiting more than eight hours.")
    lines.append("4. Monitor CSAT for the lowest-scoring categories and validate drivers before making process changes.")
    lines.append("## Limitations")
    lines.append("Data is synthetic. SLA compliance for unresolved tickets uses the configured reporting timestamp; satisfaction is missing for some tickets and is not imputed. Correlations do not establish causation.")
    Path(out).parent.mkdir(parents=True,exist_ok=True)
    Path(out).write_text("\n".join(lines))
    return out
