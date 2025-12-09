1from typing import List
2from collections import Counter
3
4class Solution:
5    def uniqueOccurrences(self, arr: List[int]) -> bool:
6        counts = Counter(arr)
7        return len(set(counts.values())) == len(counts)