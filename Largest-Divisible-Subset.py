1from typing import List
2
3class Solution:
4    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
5        if not nums:
6            return []
7
8        nums.sort()
9        n = len(nums)
10        dp = [1] * n
11        prev = [-1] * n
12
13        max_len = 1
14        max_idx = 0
15
16        for i in range(n):
17            for j in range(i):
18                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
19                    dp[i] = dp[j] + 1
20                    prev[i] = j
21            if dp[i] > max_len:
22                max_len = dp[i]
23                max_idx = i
24
25        res = []
26        while max_idx != -1:
27            res.append(nums[max_idx])
28            max_idx = prev[max_idx]
29
30        return res[::-1]