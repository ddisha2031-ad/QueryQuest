-- Consolidated operational KPI summary
-- Tables: tickets
SELECT COUNT(*) total_tickets, SUM(CASE WHEN ticket_status IN ('Open','Pending') THEN 1 ELSE 0 END) open_backlog, SUM(CASE WHEN resolved_at IS NOT NULL THEN 1 ELSE 0 END) resolved_tickets, ROUND(AVG(CASE WHEN resolved_at IS NOT NULL THEN (julianday(resolved_at)-julianday(created_at))*1440 END),1) avg_resolution_minutes, ROUND(AVG(satisfaction_score),2) avg_csat, SUM(reopened_count) reopened_tickets FROM tickets;
