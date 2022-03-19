class Solution {
public:
    string intToRoman(int num) {
      string result="";
      map<int, string> myMap;
      myMap[1]="I";
      myMap[4]="IV";
      myMap[5]="V";
      myMap[9]="IX";
      myMap[10]="X";
      myMap[40]="XL";
      myMap[50]="L";
      myMap[90]="XC";
      myMap[100]="C";
      myMap[400]="CD";
      myMap[500]="D";
      myMap[900]="CM";
      myMap[1000]="M";
      
      while(num > 0){
        for(auto itr=myMap.rbegin(); itr!=myMap.rend(); itr++){
          if(num >= itr->first){
             num-= itr->first;
             result+= itr->second;
             break;
          }
        }
      }
      return result;
    }
};