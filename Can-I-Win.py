1class Solution:
2    def canIWin(self, maxChoosableInteger, desiredTotal):
3        if desiredTotal <= 0:
4            return True
5
6        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
7        if total_sum < desiredTotal:
8            return False
9
10        memo = {}
11
12        def dfs(used, remaining):
13            if used in memo:
14                return memo[used]
15
16            for i in range(1, maxChoosableInteger + 1):
17                mask = 1 << i
18                if used & mask == 0:
19                    if i >= remaining or not dfs(used | mask, remaining - i):
20                        memo[used] = True
21                        return True
22
23            memo[used] = False
24            return False
25
26        return dfs(0, desiredTotal)