1class Solution:
2    def countCollisions(self, directions: str) -> int:
3        directions = directions.lstrip('L')
4        directions = directions.rstrip('R')
5        return len(directions) - directions.count('S')
6