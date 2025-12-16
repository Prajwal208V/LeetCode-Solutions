1class Solution:
2    def digitCount(self, num: str) -> bool:
3        from collections import Counter
4        c = Counter(num)
5        for i, ch in enumerate(num):
6            if c.get(str(i), 0) != int(ch):
7                return False
8        return True