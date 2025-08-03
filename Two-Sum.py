class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        
        for ind,num in enumerate(nums):
            complement = target - num
            if  complement in hasmap:
                return [hasmap[complement], ind]
            hasmap[num] = ind
            
            
        