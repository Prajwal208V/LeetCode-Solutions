1class Solution:
2    def magicalString(self, n):
3        if n == 0:
4            return 0
5        if n <= 3:
6            return 1
7
8        s = [1, 2, 2]
9        head = 2
10        num = 1
11        count = 1
12
13        while len(s) < n:
14            times = s[head]
15            for _ in range(times):
16                s.append(num)
17                if num == 1 and len(s) <= n:
18                    count += 1
19            num = 3 - num
20            head += 1
21
22        return count