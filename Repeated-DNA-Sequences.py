1from typing import List
2
3class Solution:
4    def findRepeatedDnaSequences(self, s: str) -> List[str]:
5        if len(s) < 10:
6            return []
7
8        mapping = {'A':0,'C':1,'G':2,'T':3}
9        seen = set()
10        repeated = set()
11        hash_val = 0
12
13        for i in range(10):
14            hash_val = (hash_val << 2) | mapping[s[i]]
15        seen.add(hash_val)
16
17        mask = (1 << 20) - 1
18
19        for i in range(10, len(s)):
20            hash_val = ((hash_val << 2) | mapping[s[i]]) & mask
21            if hash_val in seen:
22                repeated.add(s[i-9:i+1])
23            else:
24                seen.add(hash_val)
25
26        return list(repeated)