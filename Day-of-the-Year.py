1class Solution:
2    def dayOfYear(self, date: str) -> int:
3        year, month, day = map(int, date.split('-'))
4        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
5        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
6        if leap:
7            days_in_month[1] = 29
8        return sum(days_in_month[:month - 1]) + day
9