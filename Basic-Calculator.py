1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        sign = 1
5        num = 0
6        res = 0
7
8        for c in s:
9            if c.isdigit():
10                num = num * 10 + int(c)
11            elif c == '+':
12                res += sign * num
13                num = 0
14                sign = 1
15            elif c == '-':
16                res += sign * num
17                num = 0
18                sign = -1
19            elif c == '(':
20                stack.append(res)
21                stack.append(sign)
22                res = 0
23                sign = 1
24            elif c == ')':
25                res += sign * num
26                num = 0
27                res *= stack.pop()
28                res += stack.pop()
29
30        return res + sign * num
31