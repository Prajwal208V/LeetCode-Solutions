1class Solution:
2    def freqAlphabets(self, s: str) -> str:
3        res = []
4        i = 0
5        while i < len(s):
6            if i + 2 < len(s) and s[i + 2] == '#':
7                res.append(chr(int(s[i:i+2]) + 96))
8                i += 3
9            else:
10                res.append(chr(int(s[i]) + 96))
11                i += 1
12        return "".join(res)
13