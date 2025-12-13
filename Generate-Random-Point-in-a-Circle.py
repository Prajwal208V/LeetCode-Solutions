1import random
2import math
3
4class Solution:
5    def __init__(self, radius, x_center, y_center):
6        self.r = radius
7        self.x = x_center
8        self.y = y_center
9
10    def randPoint(self):
11        angle = random.uniform(0, 2 * math.pi)
12        r = self.r * math.sqrt(random.random())
13        return [self.x + r * math.cos(angle), self.y + r * math.sin(angle)]
14
15
16# Your Solution object will be instantiated and called as such:
17# obj = Solution(radius, x_center, y_center)
18# param_1 = obj.randPoint()