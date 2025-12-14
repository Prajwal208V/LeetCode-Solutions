1from typing import List
2
3class Solution:
4    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
5        boxTypes.sort(key=lambda x: x[1], reverse=True)
6        total = 0
7        
8        for boxes, units in boxTypes:
9            take = min(truckSize, boxes)
10            total += take * units
11            truckSize -= take
12            if truckSize == 0:
13                break
14        
15        return total