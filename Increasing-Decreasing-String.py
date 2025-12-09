1from collections import Counter
2
3class Solution:
4    def sortString(self, s: str) -> str:
5        cnt = Counter(s)
6        res = []
7        
8        while cnt:
9            for ch in sorted(cnt):
10                res.append(ch)
11                cnt[ch] -= 1
12                if cnt[ch] == 0:
13                    del cnt[ch]
14            
15            for ch in sorted(cnt, reverse=True):
16                res.append(ch)
17                cnt[ch] -= 1
18                if cnt[ch] == 0:
19                    del cnt[ch]
20        
21        return "".join(res)
22