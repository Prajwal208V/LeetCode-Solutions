1class Solution:
2    def maximum69Number(self, num: int) -> int:
3        s = list(str(num))
4        for i in range(len(s)):
5            if s[i] == '6':
6                s[i] = '9'
7                break
8        return int("".join(s))
9