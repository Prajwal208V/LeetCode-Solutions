class Solution {
  
public:
    vector<int> plusOne(vector<int>& digits) {
      int n=digits.size();
       int carry=1;
       for( int i=n-1;i>=0;i--){
         if(carry){
           digits[i]+=carry;
           carry=digits[i]/10;
           digits[i]%=10;
         }
         else{
           return digits;
         }
       }
      if(carry){
        digits.insert(digits.begin(),carry);
      }
      return digits;
    }
};