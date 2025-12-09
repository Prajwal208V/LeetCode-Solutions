1from typing import List
2
3class Solution:
4    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
5        if start > destination:
6            start, destination = destination, start
7        total = sum(distance)
8        clockwise = sum(distance[start:destination])
9        return min(clockwise, total - clockwise)
10