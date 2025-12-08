1class Solution:
2    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
3        need = [0] * 26
4        for c in licensePlate.lower():
5            if c.isalpha():
6                need[ord(c) - ord('a')] += 1
7
8        def covers(word: str) -> bool:
9            cnt = [0] * 26
10            for ch in word.lower():
11                if ch.isalpha():
12                    cnt[ord(ch) - ord('a')] += 1
13            for i in range(26):
14                if cnt[i] < need[i]:
15                    return False
16            return True
17
18        ans = None
19        for w in words:
20            if covers(w):
21                if ans is None or len(w) < len(ans):
22                    ans = w
23        return ans