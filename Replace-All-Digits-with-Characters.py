1class Solution:
2    def replaceDigits(self, s: str) -> str:
3        res = list(s)
4        for i in range(1, len(s), 2):
5            res[i] = chr(ord(res[i - 1]) + int(res[i]))
6        return "".join(res)