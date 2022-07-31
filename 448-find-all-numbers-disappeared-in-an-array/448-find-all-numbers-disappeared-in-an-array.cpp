class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
         int start=1;
         int end=nums.size();
         int itr=0;
         vector<int> result;
         sort( nums.begin(), nums.end() );
         nums.erase( unique( nums.begin(), nums.end() ), nums.end() );
         
         while(start<=end){
           if(start!= nums[itr]){
             result.push_back(start);
             itr--;
           }
           itr++;
           start++;
         }
      
         return result;
    }
};