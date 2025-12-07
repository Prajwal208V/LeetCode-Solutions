1class Solution:
2    def countNumbersWithUniqueDigits(self, n: int) -> int:
3        if n == 0:
4            return 1
5        ans = 10
6        cur = 9
7        available = 9
8        for i in range(2, n + 1):
9            cur *= available
10            ans += cur
11            available -= 1
12        return ans