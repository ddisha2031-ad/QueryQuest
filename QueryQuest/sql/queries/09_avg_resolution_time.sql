-- Average resolution time for resolved/closed tickets
-- Tables: tickets
SELECT ROUND(AVG((julianday(resolved_at)-julianday(created_at))*1440),1) AS avg_resolution_minutes, COUNT(*) AS resolved_tickets FROM tickets WHERE resolved_at IS NOT NULL;
