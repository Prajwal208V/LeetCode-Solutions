1from typing import List
2from collections import deque, defaultdict
3
4class Solution:
5    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
6        if n == 1:
7            return [0]
8
9        graph = defaultdict(list)
10        degree = [0] * n
11
12        for u, v in edges:
13            graph[u].append(v)
14            graph[v].append(u)
15            degree[u] += 1
16            degree[v] += 1
17
18        leaves = deque(i for i in range(n) if degree[i] == 1)
19
20        remaining = n
21        while remaining > 2:
22            size = len(leaves)
23            remaining -= size
24            for _ in range(size):
25                node = leaves.popleft()
26                for nei in graph[node]:
27                    degree[nei] -= 1
28                    if degree[nei] == 1:
29                        leaves.append(nei)
30
31        return list(leaves)