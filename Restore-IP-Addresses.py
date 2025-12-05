1from typing import List
2
3class Solution:
4    def restoreIpAddresses(self, s: str) -> List[str]:
5        res = []
6        n = len(s)
7        if n < 4 or n > 12:
8            return res
9        def backtrack(start, parts):
10            if len(parts) == 4:
11                if start == n:
12                    res.append('.'.join(parts))
13                return
14            for end in range(start, min(start + 3, n)):
15                if s[start] == '0' and end > start:
16                    break
17                seg = int(s[start:end+1])
18                if seg > 255:
19                    break
20                parts.append(s[start:end+1])
21                backtrack(end + 1, parts)
22                parts.pop()
23        backtrack(0, [])
24        return res