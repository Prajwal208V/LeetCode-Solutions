1from typing import List
2
3class Solution:
4    def majorityElement(self, nums: List[int]) -> List[int]:
5        if not nums:
6            return []
7
8        cand1 = cand2 = None
9        count1 = count2 = 0
10
11        for num in nums:
12            if num == cand1:
13                count1 += 1
14            elif num == cand2:
15                count2 += 1
16            elif count1 == 0:
17                cand1, count1 = num, 1
18            elif count2 == 0:
19                cand2, count2 = num, 1
20            else:
21                count1 -= 1
22                count2 -= 1
23
24        result = []
25        for c in (cand1, cand2):
26            if c is not None and nums.count(c) > len(nums) // 3:
27                result.append(c)
28
29        return result