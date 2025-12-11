1from typing import List
2
3class Solution:
4    def maximalSquare(self, matrix: List[List[str]]) -> int:
5        if not matrix or not matrix[0]:
6            return 0
7        m, n = len(matrix), len(matrix[0])
8        dp = [0] * (n + 1)
9        max_side = 0
10        for i in range(1, m + 1):
11            prev = 0
12            for j in range(1, n + 1):
13                temp = dp[j]
14                if matrix[i - 1][j - 1] == '1':
15                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
16                    if dp[j] > max_side:
17                        max_side = dp[j]
18                else:
19                    dp[j] = 0
20                prev = temp
21        return max_side * max_side
22