class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit=0;
        int minsoFar=prices[0];
      
        for(auto itr: prices){
          minsoFar=min(minsoFar,itr);
          
          int profit=itr-minsoFar;
          maxProfit=max(profit,maxProfit);
        }
      
      return maxProfit;
    }
};