class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> myMap;
      
        for(auto &itr: nums){
          if(myMap.find(itr) != myMap.end())
            myMap[itr]++;
          else
            myMap[itr]=1;
        }
      for(auto itr:myMap){
        if(itr.second>=2)
          return true; 
      }
      
      return false;
      
    }
 
};