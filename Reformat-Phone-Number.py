1class Solution:
2    def reformatNumber(self, number: str) -> str:
3        digits = [c for c in number if c.isdigit()]
4        res = []
5        i = 0
6        
7        while len(digits) - i > 4:
8            res.append("".join(digits[i:i+3]))
9            i += 3
10        
11        if len(digits) - i == 4:
12            res.append("".join(digits[i:i+2]))
13            res.append("".join(digits[i+2:i+4]))
14        else:
15            res.append("".join(digits[i:]))
16        
17        return "-".join(res)