1from typing import List
2
3class Solution:
4    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
5        cnt = 0
6        for x in arr:
7            if x % 2 == 1:
8                cnt += 1
9                if cnt == 3:
10                    return True
11            else:
12                cnt = 0
13        return False
14