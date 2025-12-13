1class Solution:
2    def isValidSerialization(self, preorder: str) -> bool:
3        slots = 1
4
5        for node in preorder.split(','):
6            slots -= 1
7            if slots < 0:
8                return False
9            if node != '#':
10                slots += 2
11
12        return slots == 0