1from typing import List
2
3class Solution:
4    def maxProduct(self, words: List[str]) -> int:
5        masks = []
6        lengths = []
7
8        for w in words:
9            mask = 0
10            for ch in w:
11                mask |= 1 << (ord(ch) - ord('a'))
12            masks.append(mask)
13            lengths.append(len(w))
14
15        ans = 0
16        n = len(words)
17        for i in range(n):
18            for j in range(i + 1, n):
19                if masks[i] & masks[j] == 0:
20                    ans = max(ans, lengths[i] * lengths[j])
21
22        return ans