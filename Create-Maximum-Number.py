1class Solution:
2    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
3        def pick(nums, t):
4            stack = []
5            drop = len(nums) - t
6            for x in nums:
7                while drop and stack and stack[-1] < x:
8                    stack.pop()
9                    drop -= 1
10                stack.append(x)
11            return stack[:t]
12
13        def greater(a, i, b, j):
14            while i < len(a) and j < len(b) and a[i] == b[j]:
15                i += 1
16                j += 1
17            if j == len(b):
18                return True
19            if i == len(a):
20                return False
21            return a[i] > b[j]
22
23        def merge(a, b):
24            i = j = 0
25            res = []
26            while i < len(a) or j < len(b):
27                if greater(a, i, b, j):
28                    res.append(a[i])
29                    i += 1
30                else:
31                    res.append(b[j])
32                    j += 1
33            return res
34
35        n1, n2 = len(nums1), len(nums2)
36        best = [0] * k
37        start = max(0, k - n2)
38        end = min(k, n1)
39        for i in range(start, end + 1):
40            p1 = pick(nums1, i)
41            p2 = pick(nums2, k - i)
42            cand = merge(p1, p2)
43            if cand > best:
44                best = cand
45        return best
46