1from typing import List
2from collections import defaultdict, deque
3
4class Solution:
5    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
6        graph = defaultdict(list)
7        for u, v in edges:
8            graph[u].append(v)
9            graph[v].append(u)
10        
11        q = deque([source])
12        seen = {source}
13        
14        while q:
15            u = q.popleft()
16            if u == destination:
17                return True
18            for v in graph[u]:
19                if v not in seen:
20                    seen.add(v)
21                    q.append(v)
22        return False