1class Solution:
2    def countPalindromicSubsequence(self, s: str) -> int:
3        first = {}
4        last = {}
5        for i, c in enumerate(s):
6            if c not in first:
7                first[c] = i
8            last[c] = i
9
10        ans = 0
11        for c in first:
12            l, r = first[c], last[c]
13            if l < r:
14                ans += len(set(s[l+1:r]))
15        return ans