/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    let min=Math.min(...nums);
    let max=Math.max(...nums);
    return gcd(min,max);
};
function gcd(a,b){
    if(a===0)
        return b;
    if(b===0)
        return a;
    if(a===b)
        return a;
    if(a>b)
        return gcd(a-b,b)
    else
        return gcd(a,b-a);
}