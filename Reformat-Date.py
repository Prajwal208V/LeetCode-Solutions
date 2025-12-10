1class Solution:
2    def reformatDate(self, date: str) -> str:
3        months = {
4            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
5            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
6            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
7        }
8        d, m, y = date.split()
9        day = ""
10        for c in d:
11            if c.isdigit():
12                day += c
13            else:
14                break
15        if len(day) == 1:
16            day = "0" + day
17        return f"{y}-{months[m]}-{day}"
18