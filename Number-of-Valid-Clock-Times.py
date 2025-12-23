1class Solution:
2    def countTime(self, time: str) -> int:
3        h, m = time.split(":")
4        hc = 0
5        mc = 0
6
7        for i in range(24):
8            if (h[0] == '?' or h[0] == str(i // 10)) and (h[1] == '?' or h[1] == str(i % 10)):
9                hc += 1
10
11        for i in range(60):
12            if (m[0] == '?' or m[0] == str(i // 10)) and (m[1] == '?' or m[1] == str(i % 10)):
13                mc += 1
14
15        return hc * mc