1from collections import Counter
2
3class Solution:
4    def equalFrequency(self, word: str) -> bool:
5        cnt = Counter(word)
6
7        for ch in list(cnt.keys()):
8            cnt[ch] -= 1
9            if cnt[ch] == 0:
10                del cnt[ch]
11
12            if len(set(cnt.values())) == 1:
13                return True
14
15            cnt[ch] = cnt.get(ch, 0) + 1
16
17        return False