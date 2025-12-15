1class Solution:
2    def numDifferentIntegers(self, word: str) -> int:
3        nums = set()
4        curr = ""
5        
6        for c in word:
7            if c.isdigit():
8                curr += c
9            elif curr:
10                nums.add(curr.lstrip('0') or '0')
11                curr = ""
12        
13        if curr:
14            nums.add(curr.lstrip('0') or '0')
15        
16        return len(nums)