-- Agent rankings using window functions
-- Tables: tickets, agents
WITH agg AS (SELECT agent_id, COUNT(*) assigned, SUM(CASE WHEN resolved_at IS NOT NULL THEN 1 ELSE 0 END) resolved, ROUND(AVG(satisfaction_score),2) avg_csat FROM tickets GROUP BY agent_id) SELECT a.agent_name, assigned, resolved, avg_csat, RANK() OVER (ORDER BY resolved DESC) resolution_rank, ROW_NUMBER() OVER (ORDER BY assigned DESC) volume_rank FROM agg JOIN agents a ON a.agent_id=agg.agent_id ORDER BY resolved DESC;
