1from typing import List
2
3class Solution:
4    def validUtf8(self, data: List[int]) -> bool:
5        remaining = 0
6
7        for num in data:
8            if remaining == 0:
9                if num >> 7 == 0:
10                    continue
11                elif num >> 5 == 0b110:
12                    remaining = 1
13                elif num >> 4 == 0b1110:
14                    remaining = 2
15                elif num >> 3 == 0b11110:
16                    remaining = 3
17                else:
18                    return False
19            else:
20                if num >> 6 != 0b10:
21                    return False
22                remaining -= 1
23
24        return remaining == 0