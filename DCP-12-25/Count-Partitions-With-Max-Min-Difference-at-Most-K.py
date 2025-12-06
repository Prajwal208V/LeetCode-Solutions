1from collections import deque
2from typing import List
3
4MOD = 10**9 + 7
5
6class Solution:
7    def countPartitions(self, nums: List[int], k: int) -> int:
8        n = len(nums)
9        dp = [0] * (n + 1)
10        pref = [0] * (n + 1)
11        dp[0] = 1
12        pref[0] = 1
13        maxd = deque()
14        mind = deque()
15        l = 0
16        for r in range(n):
17            while maxd and nums[maxd[-1]] <= nums[r]:
18                maxd.pop()
19            maxd.append(r)
20            while mind and nums[mind[-1]] >= nums[r]:
21                mind.pop()
22            mind.append(r)
23            while nums[maxd[0]] - nums[mind[0]] > k:
24                if maxd and maxd[0] == l:
25                    maxd.popleft()
26                if mind and mind[0] == l:
27                    mind.popleft()
28                l += 1
29            left_sum = pref[r] - (pref[l-1] if l > 0 else 0)
30            dp[r+1] = left_sum % MOD
31            pref[r+1] = (pref[r] + dp[r+1]) % MOD
32        return dp[n] % MOD
33