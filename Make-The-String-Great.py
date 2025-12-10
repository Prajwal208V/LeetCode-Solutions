1class Solution:
2    def makeGood(self, s: str) -> str:
3        stack = []
4        for ch in s:
5            if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
6                stack.pop()
7            else:
8                stack.append(ch)
9        return "".join(stack)