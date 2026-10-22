-- Backlog aging using CASE expression
-- Tables: tickets
SELECT priority, SUM(CASE WHEN (julianday('now')-julianday(created_at))*24<24 THEN 1 ELSE 0 END) under_1d, SUM(CASE WHEN (julianday('now')-julianday(created_at))*24 BETWEEN 24 AND 72 THEN 1 ELSE 0 END) d1_3, SUM(CASE WHEN (julianday('now')-julianday(created_at))*24 BETWEEN 72 AND 168 THEN 1 ELSE 0 END) d3_7, SUM(CASE WHEN (julianday('now')-julianday(created_at))*24>168 THEN 1 ELSE 0 END) over_7d FROM tickets WHERE ticket_status IN ('Open','Pending') GROUP BY priority;
