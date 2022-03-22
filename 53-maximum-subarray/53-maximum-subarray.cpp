class Solution {
public:
    int maxSubArray(vector<int>& nums) {  // I am using Kadane's Algorithm
        int sum=0,result=INT_MIN;
      
        for(auto &itr : nums){
          sum+=itr;
          
          result=max(sum, result);
          if(sum<0)
            sum=0;
        }
      
      return result;
    }
};