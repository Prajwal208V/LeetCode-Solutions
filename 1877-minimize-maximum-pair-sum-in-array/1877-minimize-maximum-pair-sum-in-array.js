/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((a,b)=>{
        if(a>b)
            return 1;
        if(a<b)
            return -1;
        return 0;
    })
    console.log(nums);
    let max_n=nums[0]+nums[nums.length-1];
    let start=0;
    let end=nums.length-1;
    while(start<end){
        max_n=Math.max(max_n,(nums[start]+nums[end]));
        start++;
        end--;
    }
    
    return max_n;
};