/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let arr=s.split("");
    let vowels = /[AEIOUaeiou]/gi;
    let start=0;
    let end=arr.length-1;
    while(start<end){
        if(arr[start].match(vowels)&&arr[end].match(vowels)){
            let temp=arr[start];
            arr[start++]=arr[end];
            arr[end--]=temp;
        }
        if(!arr[start].match(vowels))
            start++;
        if(!arr[end].match(vowels))
            end--;
        
    }
    return arr.join("");
};