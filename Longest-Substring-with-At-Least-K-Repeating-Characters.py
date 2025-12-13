1class Solution:
2    def longestSubstring(self, s: str, k: int) -> int:
3        if len(s) < k:
4            return 0
5
6        freq = {}
7        for ch in s:
8            freq[ch] = freq.get(ch, 0) + 1
9
10        for i, ch in enumerate(s):
11            if freq[ch] < k:
12                return max(
13                    self.longestSubstring(s[:i], k),
14                    self.longestSubstring(s[i + 1:], k)
15                )
16
17        return len(s)