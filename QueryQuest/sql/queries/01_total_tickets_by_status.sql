-- Total tickets by status
-- Tables: tickets
SELECT ticket_status, COUNT(*) AS total_tickets FROM tickets GROUP BY ticket_status ORDER BY total_tickets DESC;
