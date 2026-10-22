-- Median first-response time using ordered row numbers
-- Tables: tickets
WITH r AS (SELECT (julianday(first_response_at)-julianday(created_at))*1440 AS mins, ROW_NUMBER() OVER (ORDER BY (julianday(first_response_at)-julianday(created_at))*1440) rn, COUNT(*) OVER() n FROM tickets WHERE first_response_at IS NOT NULL) SELECT ROUND(AVG(mins),1) AS median_first_response_minutes FROM r WHERE rn IN ((n+1)/2,(n+2)/2);
