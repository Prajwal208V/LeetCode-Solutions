class Solution {
public:
    int findComplement(int num) {
       int bits=floor(log2(num)+1);
       int res=pow(2,bits)-1;
       return res^num;
    }
};