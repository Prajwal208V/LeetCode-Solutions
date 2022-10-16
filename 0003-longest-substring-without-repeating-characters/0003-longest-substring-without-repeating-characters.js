/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const map=new Map();
    let i=0;
    let ans=0;
    for(let j=0;j<s.length;j++){
        if(map.has(s[j])){
            i=Math.max(map.get(s[j]),i);
                    // console.log(map.get(s[j]));
        }
        ans=Math.max(ans,(j-i+1));
        // console.log(ans);
        map.set(s[j],j+1);
    }
    return ans;
};