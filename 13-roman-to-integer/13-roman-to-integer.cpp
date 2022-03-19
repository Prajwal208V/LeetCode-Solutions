class Solution {
public:
    int romanToInt(string s) {
        map<char,int> myMap;
        myMap['I']=1;
        myMap['V']=5;
        myMap['X']=10;
        myMap['L']=50;
        myMap['C']=100;
        myMap['D']=500;
        myMap['M']=1000;
        
        int result=0;
        int preValue=-1;
        for(int i=0;i<s.size();i++){
            int crnt_value=myMap[s[i]];
          
            if(preValue != -1 && preValue< crnt_value){
              crnt_value-= preValue;
              result-=preValue;
            }
              
            result+=crnt_value;
            preValue=crnt_value;
        }
      return result;
    }
};