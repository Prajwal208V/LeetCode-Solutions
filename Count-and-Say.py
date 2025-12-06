1class Solution:
2    def countAndSay(self, n: int) -> str:
3        s = "1"
4        for _ in range(n - 1):
5            t = []
6            i = 0
7            L = len(s)
8            while i < L:
9                j = i + 1
10                while j < L and s[j] == s[i]:
11                    j += 1
12                t.append(str(j - i))
13                t.append(s[i])
14                i = j
15            s = "".join(t)
16        return s