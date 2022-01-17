/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let str = s.replace(/[^a-z0-9]/gi,"").toLowerCase()
    let low=0;
    let high=str.length-1;
    while(low<=high){
        if(str[low++]!==str[high--])
            return false;
    }
    return true;
};