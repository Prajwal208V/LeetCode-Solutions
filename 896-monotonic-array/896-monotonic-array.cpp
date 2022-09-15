class Solution {
 
public:
    bool isMonotonic(vector<int>& nums) {
        bool increas=true;
        bool decreas=true;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]<nums[i+1])
                decreas=false;
            if(nums[i]>nums[i+1])
                increas=false;
        }
        return increas|| decreas;
    }
};