1class Solution:
2    def squareIsWhite(self, coordinates: str) -> bool:
3        col = ord(coordinates[0]) - ord('a')
4        row = int(coordinates[1]) - 1
5        return (col + row) % 2 == 1