1class Solution:
2    def getLucky(self, s: str, k: int) -> int:
3        num = "".join(str(ord(c) - 96) for c in s)
4        for _ in range(k):
5            num = str(sum(int(d) for d in num))
6        return int(num)