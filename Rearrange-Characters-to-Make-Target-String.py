1class Solution:
2    def rearrangeCharacters(self, s: str, target: str) -> int:
3        from collections import Counter
4        cs, ct = Counter(s), Counter(target)
5        return min(cs[c] // ct[c] for c in ct)