1class Solution:
2    def getMaximumGenerated(self, n: int) -> int:
3        if n == 0:
4            return 0
5        
6        nums = [0] * (n + 1)
7        nums[1] = 1
8        max_val = 1
9        
10        for i in range(2, n + 1):
11            if i % 2 == 0:
12                nums[i] = nums[i // 2]
13            else:
14                nums[i] = nums[i // 2] + nums[i // 2 + 1]
15            max_val = max(max_val, nums[i])
16        
17        return max_val