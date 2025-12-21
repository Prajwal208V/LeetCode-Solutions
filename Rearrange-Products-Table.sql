1-- Write your PostgreSQL query statement below
2SELECT product_id, 'store1' AS store, store1 AS price -- unpivot store1
3FROM Products
4WHERE store1 IS NOT NULL
5UNION ALL
6SELECT product_id, 'store2' AS store, store2 AS price -- unpivot store2
7FROM Products
8WHERE store2 IS NOT NULL
9UNION ALL
10SELECT product_id, 'store3' AS store, store3 AS price -- unpivot store3
11FROM Products
12WHERE store3 IS NOT NULL;