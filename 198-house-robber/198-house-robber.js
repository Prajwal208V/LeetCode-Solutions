/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    
    if(nums.length === 1)
        return nums[0];
    
    let prev1 = nums[0];
    let prev2 = nums[0] < nums[1] ? nums[1] : nums[0];
    let current = prev2;
    
    for(let i = 2; i < nums.length; i ++) {
        current = Math.max(prev1 + nums[i], prev2);
        prev1 = prev2;
        prev2 = current;
    }
    return current;
};