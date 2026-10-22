-- Monthly ticket volume with month-over-month change
-- Tables: tickets
WITH m AS (SELECT strftime('%Y-%m',created_at) month, COUNT(*) tickets FROM tickets GROUP BY month) SELECT month, tickets, LAG(tickets) OVER (ORDER BY month) AS prior_month, ROUND(100.0*(tickets-LAG(tickets) OVER (ORDER BY month))/LAG(tickets) OVER (ORDER BY month),1) AS mom_change_pct FROM m ORDER BY month;
