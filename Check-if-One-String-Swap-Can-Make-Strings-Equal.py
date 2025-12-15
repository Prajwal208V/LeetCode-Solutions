1class Solution:
2    def areAlmostEqual(self, s1: str, s2: str) -> bool:
3        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
4        return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])