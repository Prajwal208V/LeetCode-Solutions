1class Solution:
2    def countTriples(self, n: int) -> int:
3        sq = {i * i for i in range(1, n + 1)}
4        count = 0
5        for a in range(1, n + 1):
6            for b in range(1, n + 1):
7                if a * a + b * b in sq:
8                    count += 1
9        return count    