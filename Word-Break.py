1class Solution:
2    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
3        words = set(wordDict)
4        n = len(s)
5        max_len = max((len(w) for w in words), default=0)
6        dp = [False] * (n + 1)
7        dp[0] = True
8
9        for i in range(1, n + 1):
10            start = max(0, i - max_len)
11            for j in range(start, i):
12                if dp[j] and s[j:i] in words:
13                    dp[i] = True
14                    break
15        return dp[n]
16