1class Solution:
2    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
3        # Check each element with its top-left neighbor
4        for i in range(1, len(matrix)):
5            for j in range(1, len(matrix[0])):
6                if matrix[i][j] != matrix[i-1][j-1]:
7                    return False
8        return True