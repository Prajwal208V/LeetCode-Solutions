1class Solution:
2    def maxScore(self, s: str) -> int:
3        right_ones = s.count('1')
4        left_zeros = 0
5        max_score = 0
6        
7        for i in range(len(s) - 1):
8            if s[i] == '0':
9                left_zeros += 1
10            else:
11                right_ones -= 1
12            
13            max_score = max(max_score, left_zeros + right_ones)
14        
15        return max_score