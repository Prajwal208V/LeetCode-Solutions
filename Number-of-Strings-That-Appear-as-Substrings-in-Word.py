1from typing import List
2
3class Solution:
4    def numOfStrings(self, patterns: List[str], word: str) -> int:
5        return sum(p in word for p in patterns)