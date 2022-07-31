class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num>=0){
          long long sr=sqrt(num);
          if(sr*sr==num)
            return true;
        }
      return false;
    }
};