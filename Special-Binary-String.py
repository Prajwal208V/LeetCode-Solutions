1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        res = []
4        count = 0
5        start = 0
6
7        for i, ch in enumerate(s):
8            count += 1 if ch == '1' else -1
9            if count == 0:
10                inner = self.makeLargestSpecial(s[start + 1:i])
11                res.append("1" + inner + "0")
12                start = i + 1
13
14        res.sort(reverse=True)
15        return "".join(res)
16