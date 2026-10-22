"""Generates a reproducible synthetic customer-support dataset.

All agents, customers, teams and tickets are fictional. Deliberate data-quality
issues are introduced for demonstration and are documented in the cleaning log.
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N_TICKETS = 15000
START = pd.Timestamp("2025-01-01")
END = pd.Timestamp("2026-09-30 23:59:59")
AS_OF = pd.Timestamp("2026-10-22 18:00:00")

TEAMS = [(1,"Tier 1 Service Desk","Customer Support"),(2,"Tier 2 Technical Support","Customer Support"),
         (3,"Billing Operations","Finance Operations"),(4,"Account Management","Customer Success")]
AGENTS = [(i, f"Agent {i:03d}", (i % 4)+1, ["Junior","Mid","Senior"][i%3], "Active" if i%17 else "Inactive") for i in range(1,41)]
CUSTOMERS = [(i, ["SMB","Mid-Market","Enterprise"][i%3], ["North America","Europe","APAC","LATAM"][i%4],
              pd.Timestamp("2018-01-01")+pd.Timedelta(days=int(i*13)%2500)) for i in range(1,1201)]
SLA = [(1,"Critical",30,240),(2,"High",60,480),(3,"Medium",120,1440),(4,"Low",240,2880)]
CATEGORIES = {"Connectivity":["Outage","Slow speeds","Intermittent drops"],
              "Account & Access":["Login failure","Password reset","Permissions"],
              "Billing":["Invoice dispute","Refund request","Payment failure"],
              "Product Feature":["Bug report","Feature request","How-to question"],
              "Data & Integrations":["API error","Sync failure","Data export"]}
CHANNELS = ["Email","Web Portal","Live Chat","Phone"]
PRIORITIES = ["Critical","High","Medium","Low"]

def generate(raw_dir="data/raw"):
    rng = np.random.default_rng(SEED)
    raw = Path(raw_dir); raw.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(TEAMS, columns=["team_id","team_name","department"]).to_csv(raw/"teams.csv", index=False)
    pd.DataFrame(AGENTS, columns=["agent_id","agent_name","team_id","experience_band","active_status"]).to_csv(raw/"agents.csv", index=False)
    pd.DataFrame(CUSTOMERS, columns=["customer_id","customer_segment","region","customer_since"]).to_csv(raw/"customers.csv", index=False)
    pd.DataFrame(SLA, columns=["policy_id","priority","target_first_response_minutes","target_resolution_minutes"]).to_csv(raw/"sla_policies.csv", index=False)

    n = N_TICKETS
    created = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, int((END-START).total_seconds()), n), unit="s")
    priority = rng.choice(PRIORITIES, n, p=[.08,.22,.45,.25])
    cats = rng.choice(list(CATEGORIES), n, p=[.30,.22,.18,.18,.12])
    sub = [CATEGORIES[c][rng.integers(0,3)] for c in cats]
    channel = rng.choice(CHANNELS, n, p=[.42,.28,.20,.10])
    agent = rng.integers(1,41,n)
    team = np.array([AGENTS[a-1][2] for a in agent])
    sla_map = {"Critical":(30,240),"High":(60,480),"Medium":(120,1440),"Low":(240,2880)}
    fr_min = np.array([sla_map[p][0] for p in priority], dtype=float)
    res_min = np.array([sla_map[p][1] for p in priority], dtype=float)
    first_resp = created + pd.to_timedelta(rng.exponential(fr_min*0.8), unit="m")
    resolve = created + pd.to_timedelta(rng.exponential(res_min*0.9)+15, unit="m")
    status = rng.choice(["Resolved","Closed","Open","Pending"], n, p=[.55,.25,.15,.05])
    sat = np.round(np.clip(rng.normal(3.9,0.9,n),1,5))
    reopened = rng.choice([0,0,0,0,1], n)
    df = pd.DataFrame({
        "ticket_id":[f"T{i:06d}" for i in range(1,n+1)],
        "customer_id":rng.integers(1,1201,n),"agent_id":agent,"team_id":team,
        "created_at":created,"first_response_at":first_resp,"resolved_at":resolve,
        "ticket_status":status,"priority":priority,"category":cats,"subcategory":sub,
        "channel":channel,"policy_id":[PRIORITIES.index(p)+1 for p in priority],
        "satisfaction_score":sat,"reopened_count":reopened})
    # Unresolved tickets must not have resolution timestamps
    unresolved = df["ticket_status"].isin(["Open","Pending"])
    df.loc[unresolved,"resolved_at"] = pd.NaT
    df.loc[df["first_response_at"]>pd.Timestamp("2026-10-22 23:00:00"),"first_response_at"]=pd.NaT
    # Deliberate quality issues
    df.loc[df.sample(400, random_state=SEED).index,"satisfaction_score"]=np.nan          # missing CSAT
    df.loc[df.sample(150, random_state=SEED+1).index,"first_response_at"]=pd.NaT          # missing response
    bad = df.sample(30, random_state=SEED+2).index
    df.loc[bad,"resolved_at"] = df.loc[bad,"created_at"] - pd.Timedelta(hours=2)          # invalid timestamps
    df.loc[df.sample(60, random_state=SEED+3).index,"channel"]="email "                    # inconsistent label
    dups = df.sample(50, random_state=SEED+4).copy()                                       # duplicate records
    df = pd.concat([df,dups], ignore_index=True)
    raw.mkdir(parents=True, exist_ok=True)
    df.to_csv(raw/"tickets_raw.csv", index=False)
    return df

if __name__ == "__main__":
    generate()
    print("Synthetic dataset generated.")
