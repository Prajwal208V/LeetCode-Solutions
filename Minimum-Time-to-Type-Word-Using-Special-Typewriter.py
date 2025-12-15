1class Solution:
2    def minTimeToType(self, word: str) -> int:
3        pos = 'a'
4        time = 0
5        for c in word:
6            diff = abs(ord(c) - ord(pos))
7            time += min(diff, 26 - diff) + 1
8            pos = c
9        return time