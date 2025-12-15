1from typing import List
2
3class Solution:
4    def check(self, nums: List[int]) -> bool:
5        count = 0
6        n = len(nums)
7        
8        for i in range(n):
9            if nums[i] > nums[(i + 1) % n]:
10                count += 1
11                if count > 1:
12                    return False
13        return True