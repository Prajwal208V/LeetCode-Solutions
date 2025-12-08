1class Solution:
2    def diffWaysToCompute(self, expression: str) -> list[int]:
3        from functools import lru_cache
4
5        @lru_cache(None)
6        def solve(expr):
7            res = []
8            for i, c in enumerate(expr):
9                if c in "+-*":
10                    left = solve(expr[:i])
11                    right = solve(expr[i+1:])
12                    for a in left:
13                        for b in right:
14                            if c == '+':
15                                res.append(a + b)
16                            elif c == '-':
17                                res.append(a - b)
18                            else:
19                                res.append(a * b)
20            if not res:
21                return [int(expr)]
22            return res
23
24        return solve(expression)
25