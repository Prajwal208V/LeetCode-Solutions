1class Solution:
2    def numberOfCuts(self, n: int) -> int:
3        if n == 1:
4            return 0
5        return n if n % 2 == 1 else n // 2