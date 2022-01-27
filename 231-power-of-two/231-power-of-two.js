/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if(n===0)
        return false;
    if(Math.ceil(Math.log2(n))===Math.floor(Math.log2(n)))
        return true;
    else 
        return false;
};