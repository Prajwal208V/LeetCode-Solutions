1# The rand7() API is already defined for you.
2# def rand7():
3# @return a random integer in the range 1 to 7
4
5class Solution:
6    def rand10(self):
7        while True:
8            row = rand7()
9            col = rand7()
10            num = (row - 1) * 7 + col  # range: 1 to 49
11            if num <= 40:
12                return 1 + (num - 1) % 10
13        