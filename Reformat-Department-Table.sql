1SELECT
2    id,
3    SUM(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
4    SUM(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
5    SUM(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,
6    SUM(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,
7    SUM(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,
8    SUM(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,
9    SUM(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,
10    SUM(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,
11    SUM(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,
12    SUM(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,
13    SUM(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,
14    SUM(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue
15FROM Department
16GROUP BY id;
17
18