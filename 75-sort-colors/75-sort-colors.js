/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    nums.sort((a,b)=>{
        if(a>b)
            return 1;
        if(a<b)
            return -1;
        else 
            return 0;
    })
    return nums;
};