class Solution {
public:
    bool isPerfectSquare(int num) {
        if (ceil((double)sqrt(num)) == floor((double)sqrt(num))) {
          return true;
        }
      return false;
    }
};