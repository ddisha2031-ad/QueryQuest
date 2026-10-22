-- Ticket volume by month
-- Tables: tickets
SELECT strftime('%Y-%m', created_at) AS month, COUNT(*) AS tickets FROM tickets GROUP BY month ORDER BY month;
