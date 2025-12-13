1from collections import defaultdict
2
3class Solution:
4    def characterReplacement(self, s: str, k: int) -> int:
5        count = defaultdict(int)
6        left = 0
7        max_freq = 0
8        res = 0
9
10        for right in range(len(s)):
11            count[s[right]] += 1
12            max_freq = max(max_freq, count[s[right]])
13
14            while (right - left + 1) - max_freq > k:
15                count[s[left]] -= 1
16                left += 1
17
18            res = max(res, right - left + 1)
19
20        return res