1class Solution:
2    def generateMatrix(self, n: int) -> List[List[int]]:
3        # Create empty matrix
4        matrix = [[0] * n for _ in range(n)]
5        
6        # Define boundaries
7        left, right = 0, n - 1
8        top, bottom = 0, n - 1
9        
10        num = 1
11        max_num = n * n
12        
13        # Fill until we place all numbers
14        while num <= max_num:
15            
16            # Traverse left → right
17            for i in range(left, right + 1):
18                matrix[top][i] = num
19                num += 1
20            top += 1
21            
22            # Traverse top → bottom
23            for i in range(top, bottom + 1):
24                matrix[i][right] = num
25                num += 1
26            right -= 1
27            
28            # Traverse right → left
29            if top <= bottom:
30                for i in range(right, left - 1, -1):
31                    matrix[bottom][i] = num
32                    num += 1
33                bottom -= 1
34            
35            # Traverse bottom → top
36            if left <= right:
37                for i in range(bottom, top - 1, -1):
38                    matrix[i][left] = num
39                    num += 1
40                left += 1
41        
42        return matrix
43