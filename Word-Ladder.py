1from typing import List
2import string
3
4class Solution:
5    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
6        wordSet = set(wordList)
7        if endWord not in wordSet:
8            return 0
9        L = len(beginWord)
10        begin = {beginWord}
11        end = {endWord}
12        visited = {beginWord, endWord}
13        steps = 1
14        while begin and end:
15            if len(begin) > len(end):
16                begin, end = end, begin
17            next_level = set()
18            for word in begin:
19                for i in range(L):
20                    prefix = word[:i]
21                    suffix = word[i+1:]
22                    for c in string.ascii_lowercase:
23                        nw = prefix + c + suffix
24                        if nw in end:
25                            return steps + 1
26                        if nw in wordSet and nw not in visited:
27                            visited.add(nw)
28                            next_level.add(nw)
29            begin = next_level
30            steps += 1
31        return 0
32