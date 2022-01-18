/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let result=[];
    for(let i=0;i<numbers.length;i++){
        for(let j=i+1;j<numbers.length;j++){
            if(numbers[j]+numbers[i]===target){
                result[0]=i+1;
                result[1]=j+1;
            }
        }
    }
    return result;
};