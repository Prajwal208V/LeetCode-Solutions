1class Solution:
2    def maximumValue(self, strs: list[str]) -> int:
3        ans = 0
4        for s in strs:
5            if s.isdigit():
6                ans = max(ans, int(s))
7            else:
8                ans = max(ans, len(s))
9        return ans