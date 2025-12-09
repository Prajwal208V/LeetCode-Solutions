1class Solution:
2    def licenseKeyFormatting(self, s: str, k: int) -> str:
3        s = s.replace("-", "").upper()
4        if not s:
5            return ""
6        first = len(s) % k or k
7        parts = [s[:first]]
8        for i in range(first, len(s), k):
9            parts.append(s[i:i + k])
10        return "-".join(parts)
11