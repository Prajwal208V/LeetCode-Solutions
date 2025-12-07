1class Solution:
2    def minOperations(self, nums: list[int], k: int) -> int:
3        return sum(nums) % k
4