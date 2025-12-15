1class Solution:
2    def secondHighest(self, s: str) -> int:
3        digits = sorted({int(c) for c in s if c.isdigit()}, reverse=True)
4        return digits[1] if len(digits) > 1 else -1