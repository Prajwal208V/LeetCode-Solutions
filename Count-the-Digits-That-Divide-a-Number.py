1class Solution:
2    def countDigits(self, num: int) -> int:
3        res = 0
4        for ch in str(num):
5            d = int(ch)
6            if d != 0 and num % d == 0:
7                res += 1
8        return res