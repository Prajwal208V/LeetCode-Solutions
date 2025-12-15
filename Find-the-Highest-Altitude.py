1from typing import List
2
3class Solution:
4    def largestAltitude(self, gain: List[int]) -> int:
5        max_alt = 0
6        curr = 0
7        
8        for g in gain:
9            curr += g
10            max_alt = max(max_alt, curr)
11        
12        return max_alt