1class Solution:
2    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
3        lines = 1
4        current_width = 0
5        
6        for char in s:
7            char_width = widths[ord(char) - ord('a')]
8            
9            # Check if adding this character exceeds 100 pixels
10            if current_width + char_width > 100:
11                lines += 1
12                current_width = char_width
13            else:
14                current_width += char_width
15        
16        return [lines, current_width]