class Solution {
public:
    int xorOperation(int n, int start) {
        unsigned res=0;
        for(int i=0;i<n;i++){
          res^=(start+2*i);
        }
      return res;
    }
};