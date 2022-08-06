class Solution {
public:
    char findTheDifference(string s, string t) {
      sort(s.begin(), s.end());
      sort(t.begin(), t.end());
      int n1=s.size();
      int i=0;
      
      while(i<n1){
        if(s[i]!=t[i]){
          return t[i];
        }
        i++;
      }
      
      return t[i];
    }
};