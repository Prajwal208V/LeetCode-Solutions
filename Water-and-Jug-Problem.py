1import math
2
3class Solution:
4    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
5        if targetCapacity > jug1Capacity + jug2Capacity:
6            return False
7        if targetCapacity == 0:
8            return True
9        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0