1from typing import List
2from collections import Counter
3
4class Solution:
5    def findLucky(self, arr: List[int]) -> int:
6        cnt = Counter(arr)
7        res = -1
8        for num, freq in cnt.items():
9            if num == freq and num > res:
10                res = num
11        return res
12