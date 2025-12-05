1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left, right = 0, len(height) - 1
4        left_max, right_max = 0, 0
5        water = 0
6        while left < right:
7            if height[left] < height[right]:
8                if height[left] >= left_max:
9                    left_max = height[left]
10                else:
11                    water += left_max - height[left]
12                left += 1
13            else:
14                if height[right] >= right_max:
15                    right_max = height[right]
16                else:
17                    water += right_max - height[right]
18                right -= 1
19        return water