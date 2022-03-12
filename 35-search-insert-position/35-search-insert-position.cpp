class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
       if(nums[nums.size()-1]<target)
         return nums.size();
       int result=0;
        for(int i=1;i<nums.size();i++){
          if(nums[i-1]<target && nums[i]>=target)
            result=i;
        }
        return result;
          
    }
};