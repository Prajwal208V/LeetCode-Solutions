class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        unsigned reverseNum=0;
        for(int i=0;i<32;i++){
          reverseNum|=(n&1)<<(31-i);
          n>>=1;
        }
      return reverseNum;
    }
};