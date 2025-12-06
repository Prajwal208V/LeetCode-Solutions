1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        res = []
4        while columnNumber:
5            columnNumber -= 1
6            res.append(chr(columnNumber % 26 + ord('A')))
7            columnNumber //= 26
8        return ''.join(res[::-1])
9