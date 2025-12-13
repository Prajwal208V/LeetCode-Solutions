1class Solution:
2    def makesquare(self, matchsticks):
3        if not matchsticks or sum(matchsticks) % 4 != 0:
4            return False
5
6        side = sum(matchsticks) // 4
7        matchsticks.sort(reverse=True)
8        sides = [0] * 4
9
10        def dfs(i):
11            if i == len(matchsticks):
12                return sides[0] == sides[1] == sides[2] == side
13
14            for j in range(4):
15                if sides[j] + matchsticks[i] <= side:
16                    sides[j] += matchsticks[i]
17                    if dfs(i + 1):
18                        return True
19                    sides[j] -= matchsticks[i]
20                if sides[j] == 0:
21                    break
22            return False
23
24        return dfs(0)