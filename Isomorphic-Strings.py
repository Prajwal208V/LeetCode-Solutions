1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        m1, m2 = {}, {}
6        for a, b in zip(s, t):
7            if (a in m1 and m1[a] != b) or (b in m2 and m2[b] != a):
8                return False
9            m1[a] = b
10            m2[b] = a
11        return True
12