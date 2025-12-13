1class Solution:
2    def validIPAddress(self, queryIP):
3        if queryIP.count('.') == 3:
4            parts = queryIP.split('.')
5            for p in parts:
6                if not p or (p[0] == '0' and len(p) > 1):
7                    return "Neither"
8                if not p.isdigit() or not 0 <= int(p) <= 255:
9                    return "Neither"
10            return "IPv4"
11
12        if queryIP.count(':') == 7:
13            parts = queryIP.split(':')
14            hexdigits = "0123456789abcdefABCDEF"
15            for p in parts:
16                if not (1 <= len(p) <= 4):
17                    return "Neither"
18                for ch in p:
19                    if ch not in hexdigits:
20                        return "Neither"
21            return "IPv6"
22
23        return "Neither"