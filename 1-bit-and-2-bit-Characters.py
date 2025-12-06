1class Solution:
2    def isOneBitCharacter(self, bits: List[int]) -> bool:
3        i = 0
4        n = len(bits)
5        while i < n - 1:
6            if bits[i] == 1:
7                i += 2
8            else:
9                i += 1
10        return i == n - 1
11