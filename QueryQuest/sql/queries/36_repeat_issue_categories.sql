-- Repeat issue categories by customer
-- Tables: tickets
WITH repeats AS (SELECT customer_id, category, COUNT(*) n FROM tickets GROUP BY customer_id, category HAVING COUNT(*)>1) SELECT category, COUNT(*) repeat_customer_combinations, SUM(n) repeat_tickets FROM repeats GROUP BY category ORDER BY repeat_tickets DESC;
