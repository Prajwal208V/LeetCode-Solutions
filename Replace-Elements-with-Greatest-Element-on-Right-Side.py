1from typing import List
2
3class Solution:
4    def replaceElements(self, arr: List[int]) -> List[int]:
5        max_right = -1
6        for i in range(len(arr) - 1, -1, -1):
7            arr[i], max_right = max_right, max(max_right, arr[i])
8        return arr
9