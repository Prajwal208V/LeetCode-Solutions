1from typing import List
2
3class Solution:
4    def wiggleSort(self, nums: List[int]) -> None:
5        n = len(nums)
6        arr = sorted(nums)
7        mid = (n - 1) // 2
8
9        i = mid
10        j = n - 1
11        k = 0
12
13        while k < n:
14            nums[k] = arr[i]
15            k += 1
16            if k < n:
17                nums[k] = arr[j]
18                k += 1
19            i -= 1
20            j -= 1
21