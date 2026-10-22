-- Unresolved tickets beyond SLA resolution target
-- Tables: tickets, sla_policies
SELECT t.ticket_id, t.priority, t.category, t.team_id, ROUND((julianday('now')-julianday(t.created_at))*1440 - p.target_resolution_minutes,0) AS minutes_overdue FROM tickets t JOIN sla_policies p ON p.policy_id=t.policy_id WHERE t.resolved_at IS NULL AND (julianday('now')-julianday(t.created_at))*1440 > p.target_resolution_minutes ORDER BY minutes_overdue DESC;
