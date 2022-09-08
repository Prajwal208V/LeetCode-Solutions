class Solution {
public:
    int arrangeCoins(int n) {
        int result=0;
        for(int i=1;i<=INT_MAX;i++){
            n-=i;
            if(n>=0)
                result++;
            else
                break;
        }
        return result;
    }
};