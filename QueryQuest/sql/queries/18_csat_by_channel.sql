-- Customer satisfaction by support channel
-- Tables: tickets
SELECT channel, COUNT(satisfaction_score) AS csat_responses, ROUND(AVG(satisfaction_score),2) AS avg_csat FROM tickets WHERE satisfaction_score IS NOT NULL GROUP BY channel ORDER BY avg_csat;
