class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int check_count=1;
        int ptr2=1;
        for(int ptr=1; ptr<nums.size(); ptr++){
            if(nums[ptr] == nums[ptr-1] && check_count==1){
                nums[ptr2]=nums[ptr];
                ptr2++;
                check_count++;
            }
            else if(nums[ptr-1] != nums[ptr]){
              nums[ptr2]=nums[ptr];
              ptr2++;
              check_count=1;
            }
        }
      return ptr2;
    }
};