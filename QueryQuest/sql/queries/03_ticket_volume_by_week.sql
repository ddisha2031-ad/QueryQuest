-- Ticket volume by ISO week
-- Tables: tickets
SELECT strftime('%Y-W%W', created_at) AS week, COUNT(*) AS tickets FROM tickets GROUP BY week ORDER BY week;
