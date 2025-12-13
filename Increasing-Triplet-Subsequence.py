1from typing import List
2
3class Solution:
4    def increasingTriplet(self, nums: List[int]) -> bool:
5        first = float('inf')
6        second = float('inf')
7
8        for x in nums:
9            if x <= first:
10                first = x
11            elif x <= second:
12                second = x
13            else:
14                return True
15
16        return False