/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let len1=word1.length-1;
    let len2=word2.length-1;
    let i=0;
    let j=0;
    let result_str=[];
    while(i<=len1&&j<=len2){
        result_str.push(word1[i++]);
        result_str.push(word2[j++]);
    }
    while(i<=len1){
        result_str.push(word1[i++]);
    }
    while(j<=len2){
        result_str.push(word2[j++]);
    }
    return result_str.join("");
};