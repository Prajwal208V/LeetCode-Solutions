class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      
        vector<int> result;
        unordered_map<int, int >myMap;
      
        for(int i=0; i<nums.size(); i++){
          
           if(myMap.find(target- nums[i]) != myMap.end()){
               result.push_back(myMap[target-nums[i]]);
               result.push_back(i);
               return result;
           }
          
           myMap[nums[i]]=i;  
        }
      return result;
    }
};