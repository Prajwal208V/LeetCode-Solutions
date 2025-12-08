1class Solution:
2    def numberToWords(self, num: int) -> str:
3        if num == 0:
4            return "Zero"
5
6        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
7                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
8                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
9                    "Nineteen"]
10        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
11                "Sixty", "Seventy", "Eighty", "Ninety"]
12
13        def three(n: int) -> str:
14            if n == 0:
15                return ""
16            if n < 20:
17                return below_20[n] + " "
18            if n < 100:
19                return tens[n // 10] + " " + three(n % 10)
20            return below_20[n // 100] + " Hundred " + three(n % 100)
21
22        res = ""
23        if num >= 1_000_000_000:
24            res += three(num // 1_000_000_000) + "Billion "
25            num %= 1_000_000_000
26        if num >= 1_000_000:
27            res += three(num // 1_000_000) + "Million "
28            num %= 1_000_000
29        if num >= 1_000:
30            res += three(num // 1_000) + "Thousand "
31            num %= 1_000
32        if num > 0:
33            res += three(num)
34        return res.strip()
35