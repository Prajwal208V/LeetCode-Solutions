1class Solution:
2    def checkIfPangram(self, sentence: str) -> bool:
3        return len(set(sentence)) == 26