1from collections import Counter
2
3class Solution:
4    def unequalTriplets(self, nums: list[int]) -> int:
5        cnt = Counter(nums)
6        res = 0
7        left = 0
8        n = len(nums)
9        for v in cnt.values():
10            res += left * v * (n - left - v)
11            left += v
12        return res