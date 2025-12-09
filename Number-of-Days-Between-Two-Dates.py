1from datetime import date
2
3class Solution:
4    def daysBetweenDates(self, date1: str, date2: str) -> int:
5        y1, m1, d1 = map(int, date1.split("-"))
6        y2, m2, d2 = map(int, date2.split("-"))
7        return abs((date(y2, m2, d2) - date(y1, m1, d1)).days)
8