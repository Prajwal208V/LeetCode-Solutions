1from typing import List
2
3class Solution:
4    def calPoints(self, operations: List[str]) -> int:
5        stack = []
6        
7        for op in operations:
8            if op == "C":
9                stack.pop()
10            elif op == "D":
11                stack.append(2 * stack[-1])
12            elif op == "+":
13                stack.append(stack[-1] + stack[-2])
14            else:
15                stack.append(int(op))
16        
17        return sum(stack)
18