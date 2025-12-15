1class Solution:
2    def sortSentence(self, s: str) -> str:
3        words = s.split()
4        words.sort(key=lambda w: int(w[-1]))
5        return " ".join(w[:-1] for w in words)