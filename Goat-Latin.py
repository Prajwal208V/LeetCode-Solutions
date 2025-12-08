1class Solution:
2    def toGoatLatin(self, sentence: str) -> str:
3        vowels = set("aeiouAEIOU")
4        words = sentence.split()
5        res = []
6        for i, w in enumerate(words, 1):
7            if w[0] in vowels:
8                goat = w + "ma" + "a" * i
9            else:
10                goat = w[1:] + w[0] + "ma" + "a" * i
11            res.append(goat)
12        return " ".join(res)