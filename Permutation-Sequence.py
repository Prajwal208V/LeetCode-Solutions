1class Solution:
2    def getPermutation(self, n: int, k: int) -> str:
3        nums = [str(i) for i in range(1, n+1)]
4        fact = 1
5        for i in range(1, n):
6            fact *= i
7        k -= 1
8        res = []
9        while nums:
10            idx = k // fact if fact > 0 else 0
11            res.append(nums.pop(idx))
12            if not nums:
13                break
14            k %= fact
15            fact //= len(nums)
16        return ''.join(res)