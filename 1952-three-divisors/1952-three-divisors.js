/**
 * @param {number} n
 * @return {boolean}
 */
var isThree = function(n) {
    let count=0;
    let i=1;
    let temp=n;
    while(temp--){
        if(n%i===0)
            count++;
        i++;
    }
    if(count===3)
        return true;
    return false;
};