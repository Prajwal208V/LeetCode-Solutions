1class Solution:
2    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
3        broken = set(brokenLetters)
4        return sum(all(c not in broken for c in word) for word in text.split())