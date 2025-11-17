class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0
        
        def expandAroundCenter(left, right):
            """Expand around center and return the length of palindrome"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of palindrome found
            return right - left - 1
        
        for i in range(len(s)):
            # Check odd-length palindromes (single character center)
            len1 = expandAroundCenter(i, i)
            # Check even-length palindromes (two character center)
            len2 = expandAroundCenter(i, i + 1)
            
            # Get the maximum length found at this center
            curr_len = max(len1, len2)
            
            # Update start and end if we found a longer palindrome
            if curr_len > end - start + 1:
                start = i - (curr_len - 1) // 2
                end = i + curr_len // 2
        
        return s[start:end + 1]