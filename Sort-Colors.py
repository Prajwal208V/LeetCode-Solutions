class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_val_index = i
            for j in range(i+1, len(nums)):
                 if nums[j] < nums[min_val_index]:
                    min_val_index = j
            nums[i],nums[min_val_index] = nums[min_val_index], nums[i]
        return nums
        