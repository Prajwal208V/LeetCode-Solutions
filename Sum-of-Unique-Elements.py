1from typing import List
2
3class Solution:
4    def sumOfUnique(self, nums: List[int]) -> int:
5        freq = {}
6        for n in nums:
7            freq[n] = freq.get(n, 0) + 1
8        
9        return sum(num for num, cnt in freq.items() if cnt == 1)