1from typing import List
2from collections import deque
3
4class Solution:
5    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
6        bank_set = set(bank)
7        if end not in bank_set:
8            return -1
9
10        q = deque([(start, 0)])
11        visited = {start}
12        genes = ['A', 'C', 'G', 'T']
13
14        while q:
15            cur, steps = q.popleft()
16            if cur == end:
17                return steps
18
19            for i in range(len(cur)):
20                for g in genes:
21                    if g == cur[i]:
22                        continue
23                    nxt = cur[:i] + g + cur[i+1:]
24                    if nxt in bank_set and nxt not in visited:
25                        visited.add(nxt)
26                        q.append((nxt, steps + 1))
27
28        return -1