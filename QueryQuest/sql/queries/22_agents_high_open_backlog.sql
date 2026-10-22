-- Agents with unusually high open-ticket backlog
-- Tables: tickets, agents
WITH agg AS (SELECT agent_id, COUNT(*) assigned, SUM(CASE WHEN ticket_status IN ('Open','Pending') THEN 1 ELSE 0 END) open_backlog FROM tickets GROUP BY agent_id) SELECT a.agent_name, assigned, open_backlog, ROUND(100.0*open_backlog/assigned,1) AS open_pct, RANK() OVER (ORDER BY open_backlog DESC) AS backlog_rank FROM agg JOIN agents a ON a.agent_id=agg.agent_id WHERE assigned>=100 ORDER BY open_backlog DESC;
