1class Solution:
2    def halvesAreAlike(self, s: str) -> bool:
3        vowels = set("aeiouAEIOU")
4        mid = len(s) // 2
5        
6        left = sum(1 for c in s[:mid] if c in vowels)
7        right = sum(1 for c in s[mid:] if c in vowels)
8        
9        return left == right