/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let start_point=0;
    let end_point=numbers.length-1;
    while(numbers[start_point]+numbers[end_point]!==target){
        if(numbers[start_point]+numbers[end_point]>target)
            end_point--;
        else 
            start_point++;
    }
    return [start_point+1,end_point+1];
};