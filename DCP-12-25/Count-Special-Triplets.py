1from typing import List
2from collections import Counter
3
4class Solution:
5    def specialTriplets(self, nums: List[int]) -> int:
6        left = Counter()
7        right = Counter(nums)
8        MOD = 10**9 + 7
9        ans = 0
10
11        for x in nums:
12            right[x] -= 1
13            v = x * 2
14            ans = (ans + left[v] * right[v]) % MOD
15            left[x] += 1
16
17        return ans