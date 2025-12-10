1from typing import List
2
3class Solution:
4    def sortByReflection(self, nums: List[int]) -> List[int]:
5        def reflect(x: int) -> int:
6            if x == 0:
7                return 0
8            low = (x & -x).bit_length() - 1
9            high = x.bit_length() - 1
10            r = 0
11            for i in range(low, high + 1):
12                r = (r << 1) | ((x >> i) & 1)
13            return r
14
15        nums.sort(key=lambda x: (reflect(x), x))
16        return nums
17