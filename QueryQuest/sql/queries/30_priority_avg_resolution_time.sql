-- Average resolution time by priority
-- Tables: tickets
SELECT priority, COUNT(resolved_at) resolved_tickets, ROUND(AVG((julianday(resolved_at)-julianday(created_at))*1440),1) avg_resolution_minutes FROM tickets WHERE resolved_at IS NOT NULL GROUP BY priority ORDER BY avg_resolution_minutes;
