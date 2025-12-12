1from typing import List
2
3class Solution:
4    def candy(self, ratings: List[int]) -> int:
5        n = len(ratings)
6        if n == 0:
7            return 0
8        candies = [1] * n
9        for i in range(1, n):
10            if ratings[i] > ratings[i - 1]:
11                candies[i] = candies[i - 1] + 1
12        for i in range(n - 2, -1, -1):
13            if ratings[i] > ratings[i + 1]:
14                candies[i] = max(candies[i], candies[i + 1] + 1)
15        return sum(candies)