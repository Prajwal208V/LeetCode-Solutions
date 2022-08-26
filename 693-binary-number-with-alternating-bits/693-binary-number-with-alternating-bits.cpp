class Solution {
public:
    bool hasAlternatingBits(int n) {
        int prev=n&1;
        n=n>>1;
        while(n){
          int crnt=n&1;
          if(crnt==prev)
            return false;
          prev=crnt;
          n=n>>1;
        }
        return true;
    }
};