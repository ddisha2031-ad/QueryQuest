-- Reopened ticket rate
-- Tables: tickets
SELECT COUNT(*) AS total_tickets, SUM(reopened_count) AS reopened_tickets, ROUND(100.0*SUM(reopened_count)/COUNT(*),2) AS reopen_rate_pct FROM tickets;
