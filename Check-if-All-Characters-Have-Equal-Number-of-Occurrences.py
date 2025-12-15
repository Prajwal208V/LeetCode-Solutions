1from collections import Counter
2
3class Solution:
4    def areOccurrencesEqual(self, s: str) -> bool:
5        cnt = Counter(s)
6        return len(set(cnt.values())) == 1