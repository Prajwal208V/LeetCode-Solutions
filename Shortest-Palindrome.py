1class Solution:
2    def shortestPalindrome(self, s: str) -> str:
3        if not s:
4            return s
5        rev = s[::-1]
6        l = s + "#" + rev
7        lps = [0] * len(l)
8        for i in range(1, len(l)):
9            j = lps[i-1]
10            while j > 0 and l[i] != l[j]:
11                j = lps[j-1]
12            if l[i] == l[j]:
13                j += 1
14            lps[i] = j
15        add = rev[:len(s) - lps[-1]]
16        return add + s