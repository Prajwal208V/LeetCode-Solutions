1class Solution:
2    def minMoves(self, nums):
3        min_val = min(nums)
4        moves = 0
5        for num in nums:
6            moves += num - min_val
7        return moves