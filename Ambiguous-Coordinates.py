1class Solution:
2    def ambiguousCoordinates(self, s: str) -> List[str]:
3        def generate(s):
4            """Generate all valid number representations"""
5            if not s or (len(s) > 1 and s[0] == '0' and s[-1] == '0'):
6                return []
7            
8            if s[0] != '0' or len(s) == 1:
9                # Can be used as integer
10                res = [s]
11            else:
12                res = []
13            
14            # Try adding decimal point
15            for i in range(1, len(s)):
16                if (s[0] == '0' and i > 1) or s[-1] == '0':
17                    continue
18                res.append(s[:i] + '.' + s[i:])
19            
20            return res
21        
22        s = s[1:-1]  # Remove parentheses
23        ans = []
24        
25        for i in range(1, len(s)):
26            for x in generate(s[:i]):
27                for y in generate(s[i:]):
28                    ans.append(f'({x}, {y})')
29        
30        return ans