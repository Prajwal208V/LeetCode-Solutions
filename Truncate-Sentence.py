1class Solution:
2    def truncateSentence(self, s: str, k: int) -> str:
3        return " ".join(s.split()[:k])