1class Solution:
2    def numPrimeArrangements(self, n: int) -> int:
3        def count_primes(x: int) -> int:
4            if x < 2:
5                return 0
6            is_prime = [True] * (x + 1)
7            is_prime[0] = is_prime[1] = False
8            p = 2
9            while p * p <= x:
10                if is_prime[p]:
11                    for k in range(p * p, x + 1, p):
12                        is_prime[k] = False
13                p += 1
14            return sum(is_prime)
15
16        MOD = 10**9 + 7
17        primes = count_primes(n)
18        non_primes = n - primes
19
20        res = 1
21        for i in range(1, primes + 1):
22            res = (res * i) % MOD
23        for i in range(1, non_primes + 1):
24            res = (res * i) % MOD
25        return res