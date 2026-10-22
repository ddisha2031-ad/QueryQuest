-- Ticket distribution by category and subcategory
-- Tables: tickets
SELECT category, subcategory, COUNT(*) AS tickets FROM tickets GROUP BY category, subcategory ORDER BY tickets DESC;
