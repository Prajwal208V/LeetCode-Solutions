1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        citations.sort(reverse=True)
4        h=0
5        for i,c in enumerate(citations):
6            if c>= i+1:
7                h=i+1
8            else:
9                break
10        return h
11        