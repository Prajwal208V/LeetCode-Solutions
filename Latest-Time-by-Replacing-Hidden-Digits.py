1class Solution:
2    def maximumTime(self, time: str) -> str:
3        h1, h2, _, m1, m2 = time
4        
5        if h1 == '?':
6            h1 = '2' if h2 == '?' or h2 <= '3' else '1'
7        if h2 == '?':
8            h2 = '3' if h1 == '2' else '9'
9        if m1 == '?':
10            m1 = '5'
11        if m2 == '?':
12            m2 = '9'
13        
14        return h1 + h2 + ':' + m1 + m2