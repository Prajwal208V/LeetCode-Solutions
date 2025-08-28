class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        best = 0

        for right, chr in enumerate(s):
            if chr in last and last[chr] >= left:
                left = last[chr]+1
            
            last[chr] = right
            best = max(best, right-left +1)

        return best
