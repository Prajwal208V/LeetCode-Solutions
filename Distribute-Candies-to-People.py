1from typing import List
2
3class Solution:
4    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
5        res = [0] * num_people
6        give = 1
7        i = 0
8        while candies > 0:
9            to_give = min(give, candies)
10            res[i] += to_give
11            candies -= to_give
12            give += 1
13            i = (i + 1) % num_people
14        return res