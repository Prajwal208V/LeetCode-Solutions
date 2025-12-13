1from typing import List
2import re
3
4class Solution:
5    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
6        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
7        order = {name: i for i, name in enumerate(valid_lines)}
8        pattern = re.compile(r'^[A-Za-z0-9_]+$')
9
10        valid = []
11
12        for c, b, active in zip(code, businessLine, isActive):
13            if not active:
14                continue
15            if not c or not pattern.match(c):
16                continue
17            if b not in order:
18                continue
19            valid.append((order[b], c))
20
21        valid.sort()
22        return [c for _, c in valid]
23