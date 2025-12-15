1class Solution:
2    def minOperations(self, s: str) -> int:
3        count1 = count2 = 0
4        
5        for i, ch in enumerate(s):
6            if ch != ('0' if i % 2 == 0 else '1'):
7                count1 += 1
8            if ch != ('1' if i % 2 == 0 else '0'):
9                count2 += 1
10        
11        return min(count1, count2)