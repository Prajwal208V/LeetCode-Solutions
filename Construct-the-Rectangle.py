1import math
2from typing import List
3
4class Solution:
5    def constructRectangle(self, area: int) -> List[int]:
6        w = int(math.isqrt(area))
7        while area % w != 0:
8            w -= 1
9        return [area // w, w]
10