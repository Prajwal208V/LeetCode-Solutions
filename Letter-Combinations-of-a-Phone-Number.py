1class Solution:
2    def letterCombinations(self, digits):
3        if not digits:
4            return []
5        phone = {
6            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
7            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
8        }
9        res = []
10        def backtrack(index, path):
11            if index == len(digits):
12                res.append(path)
13                return
14            for char in phone[digits[index]]:
15                backtrack(index + 1, path + char)
16        backtrack(0, "")
17        return res