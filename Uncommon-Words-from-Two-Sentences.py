1class Solution:
2    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
3        from collections import Counter
4        c = Counter(s1.split()) + Counter(s2.split())
5        return [w for w, cnt in c.items() if cnt == 1]