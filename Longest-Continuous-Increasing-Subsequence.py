1from typing import List
2
3class Solution:
4    def findLengthOfLCIS(self, nums: List[int]) -> int:
5        if not nums:
6            return 0
7        
8        longest = 1
9        current = 1
10        
11        for i in range(1, len(nums)):
12            if nums[i] > nums[i - 1]:
13                current += 1
14                if current > longest:
15                    longest = current
16            else:
17                current = 1
18        
19        return longest
20