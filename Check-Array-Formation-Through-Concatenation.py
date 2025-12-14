1from typing import List
2
3class Solution:
4    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
5        first_map = {piece[0]: piece for piece in pieces}
6        i = 0
7        
8        while i < len(arr):
9            if arr[i] not in first_map:
10                return False
11            
12            piece = first_map[arr[i]]
13            for num in piece:
14                if i >= len(arr) or arr[i] != num:
15                    return False
16                i += 1
17        
18        return True