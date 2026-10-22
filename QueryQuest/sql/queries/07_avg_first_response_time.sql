-- Average first-response time in minutes
-- Tables: tickets
SELECT ROUND(AVG((julianday(first_response_at)-julianday(created_at))*1440),1) AS avg_first_response_minutes, COUNT(first_response_at) AS tickets_with_response FROM tickets WHERE first_response_at IS NOT NULL;
