1class Solution:
2    def maxSubarraySum(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        pref = [0] * (n + 1)
5        for i in range(n):
6            pref[i + 1] = pref[i] + nums[i]
7
8        min_pref = [float('inf')] * k
9        min_pref[0] = 0
10        ans = float('-inf')
11
12        for i in range(1, n + 1):
13            r = i % k
14            if min_pref[r] != float('inf'):
15                ans = max(ans, pref[i] - min_pref[r])
16            min_pref[r] = min(min_pref[r], pref[i])
17
18        return ans