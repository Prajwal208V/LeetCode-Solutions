1class Solution:
2    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
3        tax = 0
4        prev = 0
5        for upper, percent in brackets:
6            if income <= prev:
7                break
8            taxable = min(upper - prev, income - prev)
9            tax += taxable * percent / 100
10            prev = upper
11        return tax