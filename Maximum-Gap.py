1from typing import List
2
3class Solution:
4    def maximumGap(self, nums: List[int]) -> int:
5        n = len(nums)
6        if n < 2:
7            return 0
8        lo, hi = min(nums), max(nums)
9        if lo == hi:
10            return 0
11        bucket_size = max(1, (hi - lo) // (n - 1))
12        bucket_count = (hi - lo) // bucket_size + 1
13        mins = [float('inf')] * bucket_count
14        maxs = [float('-inf')] * bucket_count
15        for x in nums:
16            idx = (x - lo) // bucket_size
17            if x < mins[idx]:
18                mins[idx] = x
19            if x > maxs[idx]:
20                maxs[idx] = x
21        prev = lo
22        max_gap = 0
23        for i in range(bucket_count):
24            if mins[i] == float('inf'):
25                continue
26            gap = mins[i] - prev
27            if gap > max_gap:
28                max_gap = gap
29            prev = maxs[i]
30        return max_gap
31