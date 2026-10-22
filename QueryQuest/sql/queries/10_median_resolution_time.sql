-- Median resolution time for resolved/closed tickets
-- Tables: tickets
WITH r AS (SELECT (julianday(resolved_at)-julianday(created_at))*1440 AS mins, ROW_NUMBER() OVER (ORDER BY (julianday(resolved_at)-julianday(created_at))*1440) rn, COUNT(*) OVER() n FROM tickets WHERE resolved_at IS NOT NULL) SELECT ROUND(AVG(mins),1) AS median_resolution_minutes FROM r WHERE rn IN ((n+1)/2,(n+2)/2);
