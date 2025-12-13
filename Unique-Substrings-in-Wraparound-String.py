1class Solution:
2    def findSubstringInWraproundString(self, s):
3        dp = [0] * 26
4        k = 0
5
6        for i in range(len(s)):
7            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or
8                          (s[i - 1] == 'z' and s[i] == 'a')):
9                k += 1
10            else:
11                k = 1
12
13            idx = ord(s[i]) - ord('a')
14            dp[idx] = max(dp[idx], k)
15
16        return sum(dp)