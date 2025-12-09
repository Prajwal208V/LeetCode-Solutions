1from typing import List
2
3class Solution:
4    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
5        words = text.split()
6        res = []
7        for i in range(len(words) - 2):
8            if words[i] == first and words[i + 1] == second:
9                res.append(words[i + 2])
10        return res