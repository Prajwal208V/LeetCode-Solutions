1class Solution:
2    def isAdditiveNumber(self, num: str) -> bool:
3        n = len(num)
4
5        def add(a: str, b: str) -> str:
6            i, j = len(a) - 1, len(b) - 1
7            carry = 0
8            res = []
9            while i >= 0 or j >= 0 or carry:
10                x = int(a[i]) if i >= 0 else 0
11                y = int(b[j]) if j >= 0 else 0
12                s = x + y + carry
13                res.append(str(s % 10))
14                carry = s // 10
15                i -= 1
16                j -= 1
17            return ''.join(reversed(res))
18
19        for i in range(1, n):
20            for j in range(i + 1, n):
21                a, b = num[:i], num[i:j]
22                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
23                    continue
24                k = j
25                x, y = a, b
26                while k < n:
27                    s = add(x, y)
28                    if not num.startswith(s, k):
29                        break
30                    k += len(s)
31                    x, y = y, s
32                if k == n:
33                    return True
34        return False