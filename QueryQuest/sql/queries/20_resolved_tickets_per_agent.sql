-- Resolved tickets per agent
-- Tables: agents, tickets
SELECT a.agent_name, COUNT(t.ticket_id) AS resolved_tickets FROM agents a LEFT JOIN tickets t ON t.agent_id=a.agent_id AND t.resolved_at IS NOT NULL GROUP BY a.agent_id ORDER BY resolved_tickets DESC;
