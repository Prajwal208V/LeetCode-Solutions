var removeElement = function(nums, val) {
    let i = nums.length - 1;
    let j = i;

    while(j >= 0) {
        if (nums[j] === val) {
            nums[j] = nums[i];
            i--;
        }
        j--;
    }
    
    return i+1;
};