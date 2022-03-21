class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;
      
        for(auto &itr : tokens ){
          
          if(isdigit(itr[0]) || itr.size()> 1){
            myStack.push(std::stoi(itr));  //stoi() can convert to an int
            continue;
          }
          
          int b=myStack.top(); myStack.pop();
          int a=myStack.top(); myStack.pop();
          switch(itr[0]){
            case '+':
              myStack.push(a+b);
              break;
            case '-':
              myStack.push(a-b);
              break;
            case '*':
              myStack.push(a*b);
              break;
            case '/':
              myStack.push(a/b);
              break;
          }
        }
      
      return myStack.top();
    }
};