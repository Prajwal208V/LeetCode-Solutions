1class Solution:
2    def strongPasswordCheckerII(self, password: str) -> bool:
3        if len(password) < 8:
4            return False
5        
6        special = "!@#$%^&*()-+"
7        hasL = hasU = hasD = hasS = False
8        
9        for i, c in enumerate(password):
10            if i > 0 and c == password[i-1]:
11                return False
12            if c.islower(): hasL = True
13            elif c.isupper(): hasU = True
14            elif c.isdigit(): hasD = True
15            elif c in special: hasS = True
16        
17        return hasL and hasU and hasD and hasS