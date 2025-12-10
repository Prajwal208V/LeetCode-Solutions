1from typing import List
2
3class Solution:
4    def stringMatching(self, words: List[str]) -> List[str]:
5        res = []
6        for i, w in enumerate(words):
7            for j, v in enumerate(words):
8                if i != j and w in v:
9                    res.append(w)
10                    break
11        return res