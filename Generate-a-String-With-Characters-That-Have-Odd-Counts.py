1class Solution:
2    def generateTheString(self, n: int) -> str:
3        if n % 2 == 1:
4            return "a" * n
5        return "a" * (n - 1) + "b"
6