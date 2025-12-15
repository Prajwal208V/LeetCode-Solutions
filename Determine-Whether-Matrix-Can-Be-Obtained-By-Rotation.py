1from typing import List
2
3class Solution:
4    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
5        for _ in range(4):
6            mat = list(zip(*mat[::-1]))
7            if mat == list(map(tuple, target)):
8                return True
9        return False