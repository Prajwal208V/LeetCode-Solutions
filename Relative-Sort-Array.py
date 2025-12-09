1from typing import List
2
3class Solution:
4    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
5        count = {}
6        for x in arr1:
7            count[x] = count.get(x, 0) + 1
8        
9        res = []
10        for x in arr2:
11            if x in count:
12                res.extend([x] * count[x])
13                del count[x]
14        
15        remaining = sorted(count.keys())
16        for x in remaining:
17            res.extend([x] * count[x])
18        
19        return res