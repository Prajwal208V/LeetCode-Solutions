1class Solution:
2    def countPartitions(self, nums: List[int]) -> int:
3        s = sum(nums)
4        if s % 2 == 1:
5            return 0
6        return len(nums) - 1
7