1class Solution:
2    def numberOfWays(self, corridor: str) -> int:
3        MOD = 10**9 + 7
4        
5        seats = [i for i, c in enumerate(corridor) if c == 'S']
6        if len(seats) % 2 != 0 or len(seats) == 0:
7            return 0
8        
9        ways = 1
10        for i in range(2, len(seats), 2):
11            gap = seats[i] - seats[i - 1]
12            ways = (ways * gap) % MOD
13        
14        return ways