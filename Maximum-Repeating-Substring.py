1class Solution:
2    def maxRepeating(self, sequence: str, word: str) -> int:
3        count = 0
4        repeated = word
5        while repeated in sequence:
6            count += 1
7            repeated += word
8        return count