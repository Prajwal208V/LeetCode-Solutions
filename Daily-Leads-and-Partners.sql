1# Write your MySQL query statement below
2SELECT date_id, make_name, -- group keys: date and make
3COUNT(DISTINCT lead_id) AS unique_leads, -- count distinct leads
4COUNT(DISTINCT partner_id) AS unique_partners -- count distinct partners
5FROM DailySales
6GROUP BY date_id, make_name; -- aggregate per date and make
7