1class Solution:
2    def frequencySort(self, s):
3        freq = {}
4        for ch in s:
5            freq[ch] = freq.get(ch, 0) + 1
6
7        buckets = [[] for _ in range(len(s) + 1)]
8        for ch, count in freq.items():
9            buckets[count].append(ch)
10
11        res = []
12        for count in range(len(buckets) - 1, 0, -1):
13            for ch in buckets[count]:
14                res.append(ch * count)
15
16        return "".join(res)