1class Solution:
2    def compareVersion(self, version1: str, version2: str) -> int:
3        v1 = version1.split('.')
4        v2 = version2.split('.')
5        n = max(len(v1), len(v2))
6        for i in range(n):
7            a = int(v1[i]) if i < len(v1) else 0
8            b = int(v2[i]) if i < len(v2) else 0
9            if a < b:
10                return -1
11            if a > b:
12                return 1
13        return 0
14