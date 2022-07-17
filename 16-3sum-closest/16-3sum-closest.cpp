class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        int nearest=nums[0]+nums[1]+nums[2];
        for(int i=0;i<nums.size()-2;i++){
          int j=i+1,k=nums.size()-1;
          while(j<k){
            int cur=nums[i]+nums[j]+nums[k];
            if(abs(cur-target)<abs(target-nearest)){
              nearest=cur;
            }
            else if (cur>target) k--;
            else j++;
          }
        }
      return nearest;
        
    }
};