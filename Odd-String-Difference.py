1class Solution:
2    def oddString(self, words: list[str]) -> str:
3        def diff(w):
4            return tuple(ord(w[i+1]) - ord(w[i]) for i in range(len(w) - 1))
5
6        m = {}
7        for w in words:
8            d = diff(w)
9            m.setdefault(d, []).append(w)
10
11        for v in m.values():
12            if len(v) == 1:
13                return v[0]