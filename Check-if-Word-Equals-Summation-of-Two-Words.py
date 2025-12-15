1class Solution:
2    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
3        def val(w):
4            return int("".join(str(ord(c) - 97) for c in w))
5        return val(firstWord) + val(secondWord) == val(targetWord)