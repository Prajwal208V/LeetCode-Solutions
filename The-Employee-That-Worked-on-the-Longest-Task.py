1class Solution:
2    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
3        prev = 0
4        best = 0
5        ans = 0
6        for emp, t in logs:
7            dur = t - prev
8            if dur > best or (dur == best and emp < ans):
9                best = dur
10                ans = emp
11            prev = t
12        return ans