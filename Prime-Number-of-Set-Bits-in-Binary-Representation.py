1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        primes = {2, 3, 5, 7, 11, 13, 17, 19}
4        ans = 0
5        for x in range(left, right + 1):
6            if bin(x).count("1") in primes:
7                ans += 1
8        return ans