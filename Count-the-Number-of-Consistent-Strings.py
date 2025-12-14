1from typing import List
2
3class Solution:
4    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
5        allowed_set = set(allowed)
6        count = 0
7        
8        for word in words:
9            if all(ch in allowed_set for ch in word):
10                count += 1
11        
12        return count