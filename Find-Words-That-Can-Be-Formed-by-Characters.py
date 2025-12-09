1from typing import List
2from collections import Counter
3
4class Solution:
5    def countCharacters(self, words: List[str], chars: str) -> int:
6        chars_count = Counter(chars)
7        total = 0
8        for w in words:
9            w_count = Counter(w)
10            if all(w_count[c] <= chars_count[c] for c in w_count):
11                total += len(w)
12        return total
13