# Data Dictionary
| Table | Column | Type | Description |
|---|---|---|---|
| tickets | ticket_id | TEXT | Unique ticket identifier |
| tickets | customer_id | INTEGER | FK to customers |
| tickets | agent_id | INTEGER | FK to agents |
| tickets | team_id | INTEGER | FK to teams |
| tickets | created_at | TEXT | Ticket creation timestamp |
| tickets | first_response_at | TEXT | First agent response timestamp |
| tickets | resolved_at | TEXT | Resolution timestamp; NULL when unresolved |
| tickets | ticket_status | TEXT | Open, Pending, Resolved, Closed |
| tickets | priority | TEXT | Critical, High, Medium, Low |
| tickets | category / subcategory | TEXT | Issue classification |
| tickets | channel | TEXT | Email, Web Portal, Live Chat, Phone |
| tickets | policy_id | INTEGER | FK to SLA policy |
| tickets | satisfaction_score | REAL | 1-5 CSAT; nullable |
| tickets | reopened_count | INTEGER | Number of reopen events |
| agents | agent_id, agent_name, team_id, experience_band, active_status |  | Support agent attributes |
| teams | team_id, team_name, department |  | Support teams |
| customers | customer_id, customer_segment, region, customer_since |  | Customer attributes |
| sla_policies | policy_id, priority, target_first_response_minutes, target_resolution_minutes |  | SLA targets by priority |
