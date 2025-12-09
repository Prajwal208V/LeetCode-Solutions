1from collections import Counter
2
3class Solution:
4    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
5        need = Counter(ransomNote)
6        have = Counter(magazine)
7        for ch, c in need.items():
8            if have[ch] < c:
9                return False
10        return True
11