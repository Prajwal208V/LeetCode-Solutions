1class Solution:
2    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
3        n = len(words)
4        ans = float('inf')
5        for i, w in enumerate(words):
6            if w == target:
7                d = abs(i - startIndex)
8                ans = min(ans, d, n - d)
9        return -1 if ans == float('inf') else ans