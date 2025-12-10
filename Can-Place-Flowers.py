1from typing import List
2
3class Solution:
4    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
5        i = 0
6        length = len(flowerbed)
7        while i < length and n > 0:
8            if flowerbed[i] == 0:
9                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
10                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
11                if empty_left and empty_right:
12                    flowerbed[i] = 1
13                    n -= 1
14                    i += 2
15                    continue
16            i += 1
17        return n <= 0
18