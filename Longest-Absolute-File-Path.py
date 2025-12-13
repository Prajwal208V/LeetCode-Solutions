1class Solution:
2    def lengthLongestPath(self, input: str) -> int:
3        max_len = 0
4        path_len = {0: 0}
5
6        for line in input.split('\n'):
7            depth = line.count('\t')
8            name = line.lstrip('\t')
9
10            if '.' in name:
11                max_len = max(max_len, path_len[depth] + len(name))
12            else:
13                path_len[depth + 1] = path_len[depth] + len(name) + 1
14
15        return max_len
16