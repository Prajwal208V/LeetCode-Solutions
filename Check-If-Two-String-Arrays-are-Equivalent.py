1from typing import List
2
3class Solution:
4    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
5        return "".join(word1) == "".join(word2)