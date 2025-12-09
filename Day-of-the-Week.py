1import datetime
2
3class Solution:
4    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
5        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][
6            datetime.date(year, month, day).weekday()
7        ]
8