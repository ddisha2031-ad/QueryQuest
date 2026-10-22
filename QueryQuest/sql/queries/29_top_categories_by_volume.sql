-- Top issue categories by ticket volume
-- Tables: tickets
SELECT category, COUNT(*) tickets, RANK() OVER (ORDER BY COUNT(*) DESC) volume_rank FROM tickets GROUP BY category ORDER BY tickets DESC;
