1class Solution:
2    def haveConflict(self, e1: list[str], e2: list[str]) -> bool:
3        return not (e1[1] < e2[0] or e2[1] < e1[0])