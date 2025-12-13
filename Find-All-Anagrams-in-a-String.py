1from typing import List
2from collections import Counter
3
4class Solution:
5    def findAnagrams(self, s: str, p: str) -> List[int]:
6        res = []
7        if len(p) > len(s):
8            return res
9
10        p_count = Counter(p)
11        window = Counter()
12        left = 0
13
14        for right in range(len(s)):
15            window[s[right]] += 1
16
17            if right - left + 1 > len(p):
18                window[s[left]] -= 1
19                if window[s[left]] == 0:
20                    del window[s[left]]
21                left += 1
22
23            if window == p_count:
24                res.append(left)
25
26        return res