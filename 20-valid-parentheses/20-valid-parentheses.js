/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let arr=s.split("");
    return fun(arr);
};
var fun=(arr)=>{
    if(arr.length==1)
        return false;
    else if(arr[0]==')'|| arr[0]=='}'|| arr[0]==']'){
            return false;
        }
    else{
    let tem_arr=[];
    for(let i of arr){
        if(i=='('|| i=='{'|| i=='['){
            tem_arr.push(i);
        }
        else if(i==')'|| i=='}'|| i==']'){
            let t=tem_arr[tem_arr.length-1];
            if(t=='(') 
                t=')';
            else if(t=='{')
                t='}';
            else
                t=']';
            if(t==i){
               tem_arr.pop(); 
            }
            else 
                return false;
        }
    }
    if(tem_arr.length==0)
        return true;
    else 
        return false;
    }
}