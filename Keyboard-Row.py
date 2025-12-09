1from typing import List
2
3class Solution:
4    def findWords(self, words: List[str]) -> List[str]:
5        row1 = set("qwertyuiopQWERTYUIOP")
6        row2 = set("asdfghjklASDFGHJKL")
7        row3 = set("zxcvbnmZXCVBNM")
8        res = []
9        for w in words:
10            s = set(w)
11            if s <= row1 or s <= row2 or s <= row3:
12                res.append(w)
13        return res
14