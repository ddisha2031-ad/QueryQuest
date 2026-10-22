-- Customer satisfaction by issue category
-- Tables: tickets
SELECT category, COUNT(satisfaction_score) AS csat_responses, ROUND(AVG(satisfaction_score),2) AS avg_csat FROM tickets WHERE satisfaction_score IS NOT NULL GROUP BY category ORDER BY avg_csat;
