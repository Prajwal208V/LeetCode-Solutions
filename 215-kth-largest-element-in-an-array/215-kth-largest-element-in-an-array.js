/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    nums.sort((a,b)=>{
        if(a>b)
            return 1;
        if(a<b)
            return -1;
        return 0;
    })
    return nums[nums.length-k];
};