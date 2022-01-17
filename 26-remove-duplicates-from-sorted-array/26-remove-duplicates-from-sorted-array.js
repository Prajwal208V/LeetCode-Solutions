/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let pointer=0;
    for(let i=0;i<nums.length;i++){
        let teamp=nums[pointer];
        if(teamp!==nums[i]){
            pointer++;
            nums[pointer]=nums[i];
        }
    }
    return pointer+1;
};