1from typing import List
2from collections import Counter
3
4class Solution:
5    def numIdenticalPairs(self, nums: List[int]) -> int:
6        c = Counter(nums)
7        ans = 0
8        for v in c.values():
9            ans += v * (v - 1) // 2
10        return ans
11