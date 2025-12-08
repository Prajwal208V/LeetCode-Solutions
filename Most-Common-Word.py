1class Solution:
2    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
3        banned_set = set(banned)
4        word = []
5        freq = {}
6        for c in paragraph.lower():
7            if c.isalpha():
8                word.append(c)
9            elif word:
10                w = ''.join(word)
11                if w not in banned_set:
12                    freq[w] = freq.get(w, 0) + 1
13                word = []
14        if word:
15            w = ''.join(word)
16            if w not in banned_set:
17                freq[w] = freq.get(w, 0) + 1
18        best_word = ""
19        best_count = 0
20        for w, c in freq.items():
21            if c > best_count:
22                best_count = c
23                best_word = w
24        return best_word
25