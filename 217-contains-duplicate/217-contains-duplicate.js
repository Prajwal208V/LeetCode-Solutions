/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let new_arr=new Set(nums);
    if(nums.length===new_arr.size)
        return false;
    else 
        return true;
};