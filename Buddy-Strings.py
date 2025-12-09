1class Solution:
2    def buddyStrings(self, s: str, goal: str) -> bool:
3        if len(s) != len(goal) or len(s) < 2:
4            return False
5        
6        if s == goal:
7            return len(set(s)) < len(s)
8        
9        diff = []
10        for i in range(len(s)):
11            if s[i] != goal[i]:
12                diff.append(i)
13                if len(diff) > 2:
14                    return False
15        
16        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
17