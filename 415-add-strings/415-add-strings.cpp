class Solution {
public:
    string addStrings(string num1, string num2) {
        int x=num1.size()-1,y=num2.size()-1;
        string res;
        int carry=0;
        while(x>=0||y>=0){
            int sum=carry;
            if(x>=0)
                sum+=num1[x--]-'0';
            if(y>=0)
                sum+=num2[y--]-'0';
            carry=sum>9?1:0;
            res+=to_string(sum%10);
        }
        if(carry) res+=to_string(carry);
        reverse(res.begin(),res.end());
        return res;
    }
};