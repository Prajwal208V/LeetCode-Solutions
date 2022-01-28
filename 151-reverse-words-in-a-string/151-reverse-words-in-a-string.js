/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let arr=s.split(" ").filter((a)=> a!=='');
    arr.reverse();
    return arr.join(" ");
};