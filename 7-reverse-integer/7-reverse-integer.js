/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let neg=0;
    let result=0;
    if(x<0){
        x*=-1;
        neg=1;
    }
    while(x){
      let rem=x%10;
      result=(result*10)+(rem);
      x=Math.floor(x/10);
    }
    if(result>=(Math.pow(2,31)-1) )
        return 0;
    if(neg===0)
        return result;
    else 
        return result*-1;
    
};