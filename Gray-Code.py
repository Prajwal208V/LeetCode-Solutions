1from typing import List
2
3class Solution:
4    def grayCode(self, n: int) -> List[int]:
5        return [i ^ (i >> 1) for i in range(1 << n)]
6