1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        if not matrix or not matrix[0]:
4            return 0  # Handle empty matrix case
5
6        max_area = 0  # Store the maximal rectangle area found
7        n = len(matrix[0])  # Number of columns
8        heights = [0] * n  # Initialize heights array for histogram
9
10        for row in matrix:
11            for i in range(n):
12                if row[i] == '1':
13                    heights[i] += 1  # Increment height if '1'
14                else:
15                    heights[i] = 0  # Reset height if '0'
16
17            stack = []  # Stack to store indices
18            for i in range(n + 1):
19                cur_height = heights[i] if i < n else 0  # Add a zero height at the end
20                while stack and cur_height < heights[stack[-1]]:
21                    h = heights[stack.pop()]  # Height of the rectangle
22                    w = i if not stack else i - stack[-1] - 1  # Width of the rectangle
23                    max_area = max(max_area, h * w)  # Update max_area if needed
24                stack.append(i)  # Push current index to stack
25
26        return max_area  # Return the largest area found