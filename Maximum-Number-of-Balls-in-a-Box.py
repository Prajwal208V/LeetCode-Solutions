1class Solution:
2    def countBalls(self, lowLimit: int, highLimit: int) -> int:
3        box = {}
4        
5        for i in range(lowLimit, highLimit + 1):
6            s = sum(map(int, str(i)))
7            box[s] = box.get(s, 0) + 1
8        
9        return max(box.values())