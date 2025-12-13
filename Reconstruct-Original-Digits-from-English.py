1from collections import Counter
2
3class Solution:
4    def originalDigits(self, s: str) -> str:
5        cnt = Counter(s)
6        res = [0] * 10
7
8        res[0] = cnt['z']
9        res[2] = cnt['w']
10        res[4] = cnt['u']
11        res[6] = cnt['x']
12        res[8] = cnt['g']
13
14        res[3] = cnt['h'] - res[8]
15        res[5] = cnt['f'] - res[4]
16        res[7] = cnt['s'] - res[6]
17        res[1] = cnt['o'] - res[0] - res[2] - res[4]
18        res[9] = cnt['i'] - res[5] - res[6] - res[8]
19
20        ans = []
21        for i in range(10):
22            ans.append(str(i) * res[i])
23
24        return ''.join(ans)