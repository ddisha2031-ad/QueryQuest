-- Open tickets grouped by backlog age
-- Tables: tickets
SELECT CASE WHEN (julianday('now')-julianday(created_at))*24 < 24 THEN '0-24 hours' WHEN (julianday('now')-julianday(created_at))*24 < 72 THEN '1-3 days' WHEN (julianday('now')-julianday(created_at))*24 < 168 THEN '3-7 days' WHEN (julianday('now')-julianday(created_at))*24 < 720 THEN '7-30 days' ELSE '30+ days' END AS age_band, COUNT(*) AS open_tickets FROM tickets WHERE ticket_status IN ('Open','Pending') GROUP BY age_band ORDER BY MIN((julianday('now')-julianday(created_at))*24);
