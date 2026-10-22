-- Ticket assignments and open backlog by agent
-- Tables: agents, tickets, teams
SELECT a.agent_name, tm.team_name, COUNT(t.ticket_id) AS assigned_tickets, SUM(CASE WHEN t.ticket_status IN ('Open','Pending') THEN 1 ELSE 0 END) AS open_backlog FROM agents a LEFT JOIN tickets t ON t.agent_id=a.agent_id LEFT JOIN teams tm ON tm.team_id=a.team_id GROUP BY a.agent_id ORDER BY assigned_tickets DESC;
