class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_val = 0
        for num in nums:
            single_val ^= num
        return single_val
        