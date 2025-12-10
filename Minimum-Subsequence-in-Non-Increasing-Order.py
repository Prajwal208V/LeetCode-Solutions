1from typing import List
2
3class Solution:
4    def minSubsequence(self, nums: List[int]) -> List[int]:
5        nums.sort(reverse=True)
6        total = sum(nums)
7        cur = 0
8        res = []
9        for x in nums:
10            cur += x
11            res.append(x)
12            if cur > total - cur:
13                break
14        return res
15