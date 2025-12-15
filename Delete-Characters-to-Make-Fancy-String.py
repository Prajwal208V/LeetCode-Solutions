1class Solution:
2    def makeFancyString(self, s: str) -> str:
3        res = []
4        for c in s:
5            if len(res) < 2 or not (res[-1] == res[-2] == c):
6                res.append(c)
7        return "".join(res)