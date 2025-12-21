1from typing import List
2
3class Solution:
4    def minDeletionSize(self, strs: List[str]) -> int:
5        n = len(strs)
6        m = len(strs[0])
7        
8        # Tracks whether each adjacent row pair is already sorted
9        sorted_pairs = [False] * (n - 1)
10        deletions = 0
11        
12        for col in range(m):
13            bad = False
14            
15            # Check if this column breaks sorting
16            for i in range(n - 1):
17                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
18                    bad = True
19                    break
20            
21            if bad:
22                deletions += 1
23                continue
24            
25            # Update sorted status
26            for i in range(n - 1):
27                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
28                    sorted_pairs[i] = True
29        
30        return deletions