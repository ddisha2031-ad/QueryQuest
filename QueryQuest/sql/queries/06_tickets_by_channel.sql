-- Ticket volume by support channel
-- Tables: tickets
SELECT channel, COUNT(*) AS tickets, ROUND(100.0*COUNT(*)/SUM(COUNT(*)) OVER(),2) AS pct FROM tickets GROUP BY channel ORDER BY tickets DESC;
