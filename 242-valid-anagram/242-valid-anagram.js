/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!==t.length)
        return false;
    let mapr={};
    for(let char of s){
        if(mapr[char]===undefined)
            mapr[char]=0;
        mapr[char]++;
    }
    for(let char of t){
        if(mapr[char]===undefined)
            return false;
        mapr[char]--;
        if(mapr[char]===0)
            mapr[char]=undefined;
    }
    return true;
};