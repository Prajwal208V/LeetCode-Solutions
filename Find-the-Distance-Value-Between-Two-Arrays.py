1from typing import List
2import bisect
3
4class Solution:
5    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
6        arr2.sort()
7        res = 0
8        for x in arr1:
9            i = bisect.bisect_left(arr2, x)
10            ok = True
11            if i < len(arr2) and abs(arr2[i] - x) <= d:
12                ok = False
13            if i > 0 and abs(arr2[i - 1] - x) <= d:
14                ok = False
15            if ok:
16                res += 1
17        return res
18