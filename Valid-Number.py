1class Solution:
2    def isNumber(self, s: str) -> bool:
3        s = s.strip()
4        num = dot = exp = sign = False
5        for i, c in enumerate(s):
6            if c.isdigit():
7                num = True
8            elif c in "+-":
9                if i > 0 and s[i-1] not in "eE":
10                    return False
11            elif c == ".":
12                if dot or exp:
13                    return False
14                dot = True
15            elif c in "eE":
16                if exp or not num:
17                    return False
18                exp = True
19                num = False
20            else:
21                return False
22        return num
23