-- Workload distribution by team
-- Tables: tickets, teams
SELECT tm.team_name, COUNT(t.ticket_id) tickets, ROUND(100.0*COUNT(t.ticket_id)/SUM(COUNT(t.ticket_id)) OVER(),1) pct_of_volume, COUNT(DISTINCT t.agent_id) active_agents, ROUND(1.0*COUNT(t.ticket_id)/COUNT(DISTINCT t.agent_id),1) tickets_per_agent FROM tickets t JOIN teams tm ON tm.team_id=t.team_id GROUP BY tm.team_name ORDER BY tickets DESC;
