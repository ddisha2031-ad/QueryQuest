-- High-priority unresolved tickets
-- Tables: tickets
SELECT ticket_id, priority, category, channel, created_at, ROUND((julianday('now')-julianday(created_at))*24,1) AS age_hours FROM tickets WHERE priority IN ('Critical','High') AND ticket_status IN ('Open','Pending') ORDER BY age_hours DESC;
