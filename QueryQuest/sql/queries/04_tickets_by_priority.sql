-- Ticket distribution by priority
-- Tables: tickets
SELECT priority, COUNT(*) AS tickets, ROUND(100.0*COUNT(*)/SUM(COUNT(*)) OVER(),2) AS pct_of_total FROM tickets GROUP BY priority ORDER BY tickets DESC;
