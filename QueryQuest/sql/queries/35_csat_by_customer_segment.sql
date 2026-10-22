-- Customer satisfaction by customer segment
-- Tables: tickets, customers
SELECT c.customer_segment, COUNT(t.satisfaction_score) responses, ROUND(AVG(t.satisfaction_score),2) avg_csat FROM tickets t JOIN customers c ON c.customer_id=t.customer_id WHERE t.satisfaction_score IS NOT NULL GROUP BY c.customer_segment ORDER BY avg_csat;
