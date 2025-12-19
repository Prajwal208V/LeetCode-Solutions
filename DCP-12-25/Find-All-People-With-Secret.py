1from typing import List
2from collections import defaultdict
3
4class Solution:
5    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
6        parent = list(range(n))
7
8        def find(x):
9            while parent[x] != x:
10                parent[x] = parent[parent[x]]
11                x = parent[x]
12            return x
13
14        def union(x, y):
15            px, py = find(x), find(y)
16            if px != py:
17                parent[py] = px
18
19        # Person 0 and firstPerson know the secret initially
20        union(0, firstPerson)
21
22        meetings.sort(key=lambda x: x[2])
23
24        i = 0
25        while i < len(meetings):
26            time = meetings[i][2]
27            temp = []
28
29            # Process all meetings at the same time
30            while i < len(meetings) and meetings[i][2] == time:
31                x, y, _ = meetings[i]
32                union(x, y)
33                temp.append((x, y))
34                i += 1
35
36            # Rollback connections if not connected to person 0
37            for x, y in temp:
38                if find(x) != find(0):
39                    parent[x] = x
40                    parent[y] = y
41
42        return [i for i in range(n) if find(i) == find(0)]