-- Peak ticket arrival hours
-- Tables: tickets
SELECT strftime('%H',created_at) AS hour_of_day, COUNT(*) AS tickets FROM tickets GROUP BY hour_of_day ORDER BY CAST(hour_of_day AS INTEGER);
