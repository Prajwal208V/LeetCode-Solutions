class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int n=nums.size();
        if(n==0)
            return{-1,-1};
        int left=0,right=n-1,mid;
        while(left<right){
            mid=(left+right)/2;
            if(target>nums[mid])
                left=mid+1;
            else 
                right=mid;
        }
        int lower=left;
        if(nums[lower]!=target)
            return {-1,-1};
        left=0;
        right=n;
        while(left<right){
            mid=(left+right)/2;
            if(target>=nums[mid])
                left=mid+1;
            else 
                right=mid;
        }
        int heigher=left-1;
        return {lower,heigher};
    }
};