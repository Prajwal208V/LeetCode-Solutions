class Solution {
public:
    int minBitFlips(int start, int goal) {
        int bits= start^goal;
        int diff=0;
        while(bits){
            diff++;
            bits=(bits)&(bits-1);
        }
        return diff;
    }
};