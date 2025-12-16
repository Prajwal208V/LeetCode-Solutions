1from typing import List
2from math import inf
3
4fmax = lambda x, y: x if x > y else y
5
6def merge(A, B):
7    C = [-inf] * len(A)
8    for i, a in enumerate(A):
9        if a < 0:
10            continue
11        for j in range(len(A) - i):
12            C[i + j] = fmax(C[i + j], a + B[j])
13    return C
14
15class Solution:
16    def maxProfit(
17        self,
18        n: int,
19        present: List[int],
20        future: List[int],
21        hierarchy: List[List[int]],
22        budget: int,
23    ) -> int:
24
25        adj = [[] for _ in range(n)]
26        for u, v in hierarchy:
27            adj[u - 1].append(v - 1)
28
29        def dfs(u):
30            # dp0[b]: parent NOT bought
31            # dp1[b]: parent BOUGHT
32            dp0 = [0] * (budget + 1)
33            dp1 = [0] * (budget + 1)
34
35            for v in adj[u]:
36                c0, c1 = dfs(v)
37                dp0 = merge(dp0, c0)
38                dp1 = merge(dp1, c1)
39
40            ans0 = dp0[:]   # skip u
41            ans1 = dp0[:]   # skip u even if discounted
42
43            # buy u (no discount)
44            cost = present[u]
45            profit = future[u] - cost
46            for b in range(cost, budget + 1):
47                ans0[b] = fmax(ans0[b], dp1[b - cost] + profit)
48
49            # buy u (discount)
50            cost //= 2
51            profit = future[u] - cost
52            for b in range(cost, budget + 1):
53                ans1[b] = fmax(ans1[b], dp1[b - cost] + profit)
54
55            return ans0, ans1
56
57        return max(dfs(0)[0])