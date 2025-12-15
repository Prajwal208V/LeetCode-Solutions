1class Solution:
2    def checkZeroOnes(self, s: str) -> bool:
3        max1 = max0 = cur1 = cur0 = 0
4        for c in s:
5            if c == '1':
6                cur1 += 1
7                cur0 = 0
8            else:
9                cur0 += 1
10                cur1 = 0
11            max1 = max(max1, cur1)
12            max0 = max(max0, cur0)
13        return max1 > max0