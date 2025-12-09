1from typing import List
2
3class Solution:
4    def duplicateZeros(self, arr: List[int]) -> None:
5        """
6        Do not return anything, modify arr in-place instead.
7        """
8        n = len(arr)
9        zeros = arr.count(0)
10        i = n - 1
11        j = n + zeros - 1
12
13        while i < j:
14            if j < n:
15                arr[j] = arr[i]
16            if arr[i] == 0:
17                j -= 1
18                if j < n:
19                    arr[j] = 0
20            i -= 1
21            j -= 1
22        