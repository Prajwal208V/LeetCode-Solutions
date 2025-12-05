1from typing import List
2
3class Solution:
4    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
5        if len(arr) <= 2:
6            return True
7        arr.sort()
8        d = arr[1] - arr[0]
9        for i in range(2, len(arr)):
10            if arr[i] - arr[i-1] != d:
11                return False
12        return True
13