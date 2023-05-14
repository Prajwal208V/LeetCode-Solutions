class Solution {
public:
    void reverseString(vector<char>& s,int left=0,int right = -1) {
        if(right == -1)
            right=s.size()-1;
        if(left > right)
            return;
        int temp=s[left];
        s[left]=s[right];
        s[right]=temp;
        reverseString(s,left+1,right-1);
    }
};