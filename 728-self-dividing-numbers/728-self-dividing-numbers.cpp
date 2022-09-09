class Solution {
private:
     bool isDivide(int x){
         int temp=x;
         while(temp!=0){
             int rem=temp%10;
             if(rem==0|| x%rem!=0)
                 return false;
             temp/=10;
         }
         return true;
     }
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for(int i=left;i<=right;i++){
            if(isDivide(i))
                res.push_back(i);
        }
        return res;
        
    }
};