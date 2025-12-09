1from typing import List
2from collections import Counter
3from math import gcd
4
5class Solution:
6    def hasGroupsSizeX(self, deck: List[int]) -> bool:
7        count = Counter(deck)
8        g = 0
9        for c in count.values():
10            g = gcd(g, c)
11        return g >= 2
12