1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4# The isBadVersion API is already defined for you.
5# def isBadVersion(version: int) -> bool:
6
7class Solution:
8    def firstBadVersion(self, n: int) -> int:
9        left, right = 1, n
10        while left < right:
11            mid = (left + right) // 2
12            if isBadVersion(mid):
13                right = mid
14            else:
15                left = mid + 1
16        return left
17