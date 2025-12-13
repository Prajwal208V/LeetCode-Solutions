1class Solution:
2    def getHint(self, secret: str, guess: str) -> str:
3        bulls = 0
4        count = [0] * 10
5        cows = 0
6
7        for s, g in zip(secret, guess):
8            if s == g:
9                bulls += 1
10            else:
11                if count[int(s)] < 0:
12                    cows += 1
13                if count[int(g)] > 0:
14                    cows += 1
15                count[int(s)] += 1
16                count[int(g)] -= 1
17
18        return f"{bulls}A{cows}B" 