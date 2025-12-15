1from typing import List
2
3class Solution:
4    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
5        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
6        return sum(1 for item in items if item[idx] == ruleValue)