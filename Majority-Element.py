1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        count = 0
4        candidate = 0
5        for x in nums:
6            if count == 0:
7                candidate = x
8            count += 1 if x == candidate else -1
9        return candidate
10