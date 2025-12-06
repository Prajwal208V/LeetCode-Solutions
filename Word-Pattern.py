1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        words = s.split()
4        if len(pattern) != len(words):
5            return False
6        p2w = {}
7        w2p = {}
8        for p, w in zip(pattern, words):
9            if p in p2w and p2w[p] != w:
10                return False
11            if w in w2p and w2p[w] != p:
12                return False
13            p2w[p] = w
14            w2p[w] = p
15        return True