1class Solution:
2    def isCircularSentence(self, sentence: str) -> bool:
3        words = sentence.split()
4        for i in range(len(words)):
5            if words[i][-1] != words[(i + 1) % len(words)][0]:
6                return False
7        return True