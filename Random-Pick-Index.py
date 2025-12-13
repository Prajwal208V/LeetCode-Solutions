1import random
2from typing import List
3from collections import defaultdict
4
5class Solution:
6    def __init__(self, nums: List[int]):
7        self.pos = defaultdict(list)
8        for i, v in enumerate(nums):
9            self.pos[v].append(i)
10
11    def pick(self, target: int) -> int:
12        return random.choice(self.pos[target])
13
14# Your Solution object will be instantiated and called as such:
15# obj = Solution(nums)
16# param_1 = obj.pick(target)