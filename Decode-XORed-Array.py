1from typing import List
2
3class Solution:
4    def decode(self, encoded: List[int], first: int) -> List[int]:
5        res = [first]
6        
7        for e in encoded:
8            res.append(res[-1] ^ e)
9        
10        return res