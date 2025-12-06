1class Solution:
2    def findPairs(self, nums: List[int], k: int) -> int:
3        if k < 0:
4            return 0
5        from collections import Counter
6        cnt = Counter(nums)
7        if k == 0:
8            return sum(1 for v in cnt.values() if v > 1)
9        s = set(cnt.keys())
10        return sum(1 for x in s if x + k in s)