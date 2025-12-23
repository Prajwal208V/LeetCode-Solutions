1class Solution:
2    def averageValue(self, nums: list[int]) -> int:
3        arr = [x for x in nums if x % 6 == 0]
4        return sum(arr) // len(arr) if arr else 0