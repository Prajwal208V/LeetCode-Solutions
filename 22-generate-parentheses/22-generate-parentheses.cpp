class Solution {
public:
    vector<string> myVect;
  
    void generator(int open, int close, string ans){
      
        if(open==0 && close==0){
          myVect.push_back(ans);
          return;
        }
      
        if(open>0){
           ans.push_back('('); 
           generator(open-1, close, ans);
           ans.pop_back();
        }
      
        if(close>0 && open<close){
           ans.push_back(')');
           generator(open, close-1, ans);
           ans.pop_back();
        }
    }
  
    vector<string> generateParenthesis(int n) {
        generator(n,n,"");
        return myVect;
    }
};