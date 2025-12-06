1class Solution:
2    def minSubarray(self, nums: list[int], p: int) -> int:
3        total_mod = sum(nums) % p
4        if total_mod == 0:
5            return 0
6
7        seen = {0: -1}            # mod -> latest index (start with prefix 0 at index -1)
8        cur = 0
9        best = len(nums)         # best length found
10
11        for i, v in enumerate(nums):
12            cur = (cur + v) % p
13            need = (cur - total_mod) % p
14            if need in seen:
15                best = min(best, i - seen[need])
16            # overwrite to keep the most recent index for this mod
17            seen[cur] = i
18
19        return -1 if best == len(nums) else best
20