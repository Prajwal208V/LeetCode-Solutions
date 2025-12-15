1class Solution:
2    def largestOddNumber(self, num: str) -> str:
3        for i in range(len(num) - 1, -1, -1):
4            if int(num[i]) % 2 == 1:
5                return num[:i + 1]
6        return ""