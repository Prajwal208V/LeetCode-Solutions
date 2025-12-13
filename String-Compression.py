1class Solution:
2    def compress(self, chars):
3        write = 0
4        read = 0
5        n = len(chars)
6
7        while read < n:
8            ch = chars[read]
9            count = 0
10
11            while read < n and chars[read] == ch:
12                read += 1
13                count += 1
14
15            chars[write] = ch
16            write += 1
17
18            if count > 1:
19                for digit in str(count):
20                    chars[write] = digit
21                    write += 1
22
23        return write