1from typing import List
2
3class Solution:
4    def sortByBits(self, arr: List[int]) -> List[int]:
5        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
6