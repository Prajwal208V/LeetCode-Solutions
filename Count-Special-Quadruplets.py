1from typing import List
2
3class Solution:
4    def countQuadruplets(self, nums: List[int]) -> int:
5        n = len(nums)
6        cnt = 0
7        for a in range(n):
8            for b in range(a + 1, n):
9                for c in range(b + 1, n):
10                    for d in range(c + 1, n):
11                        if nums[a] + nums[b] + nums[c] == nums[d]:
12                            cnt += 1
13        return cnt 