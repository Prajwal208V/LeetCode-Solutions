1class Solution:
2    def findNthDigit(self, n: int) -> int:
3        digit_len = 1
4        count = 9
5        start = 1
6
7        while n > digit_len * count:
8            n -= digit_len * count
9            digit_len += 1
10            count *= 10
11            start *= 10
12
13        num = start + (n - 1) // digit_len
14        return int(str(num)[(n - 1) % digit_len])