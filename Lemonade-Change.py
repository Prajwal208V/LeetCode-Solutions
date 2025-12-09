1from typing import List
2
3class Solution:
4    def lemonadeChange(self, bills: List[int]) -> bool:
5        five = 0
6        ten = 0
7        
8        for b in bills:
9            if b == 5:
10                five += 1
11            elif b == 10:
12                if five == 0:
13                    return False
14                five -= 1
15                ten += 1
16            else:
17                if ten > 0 and five > 0:
18                    ten -= 1
19                    five -= 1
20                elif five >= 3:
21                    five -= 3
22                else:
23                    return False
24        
25        return True