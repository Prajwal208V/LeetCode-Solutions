1from typing import List
2from collections import Counter
3
4class Solution:
5    def makeEqual(self, words: List[str]) -> bool:
6        total_chars = Counter("".join(words))
7        n = len(words)
8        
9        for count in total_chars.values():
10            if count % n != 0:
11                return False
12        
13        return True