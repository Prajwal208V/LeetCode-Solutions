1class Solution:
2    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
3        if numerator == 0:
4            return "0"
5        res = []
6        if (numerator < 0) ^ (denominator < 0):
7            res.append('-')
8        numerator, denominator = abs(numerator), abs(denominator)
9        res.append(str(numerator // denominator))
10        remainder = numerator % denominator
11        if remainder == 0:
12            return ''.join(res)
13        res.append('.')
14        seen = {}
15        while remainder:
16            if remainder in seen:
17                idx = seen[remainder]
18                res.insert(idx, '(')
19                res.append(')')
20                break
21            seen[remainder] = len(res)
22            remainder *= 10
23            res.append(str(remainder // denominator))
24            remainder %= denominator
25        return ''.join(res)
26