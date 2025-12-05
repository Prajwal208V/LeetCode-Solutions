1from collections import deque
2from typing import List
3
4class Solution:
5    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
6        indeg = [0] * numCourses
7        adj = [[] for _ in range(numCourses)]
8        for a, b in prerequisites:
9            adj[b].append(a)
10            indeg[a] += 1
11        q = deque([i for i in range(numCourses) if indeg[i] == 0])
12        seen = 0
13        while q:
14            node = q.popleft()
15            seen += 1
16            for nei in adj[node]:
17                indeg[nei] -= 1
18                if indeg[nei] == 0:
19                    q.append(nei)
20        return seen == numCourses
21