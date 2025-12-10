1from typing import List
2
3class Solution:
4    def restoreString(self, s: str, indices: List[int]) -> str:
5        res = [''] * len(s)
6        for c, i in zip(s, indices):
7            res[i] = c
8        return ''.join(res)