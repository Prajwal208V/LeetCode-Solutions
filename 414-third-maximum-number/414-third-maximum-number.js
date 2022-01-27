/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let set1=new Set(nums);
    nums=[...set1];
    if(nums.length<3)
        return Math.max(...nums);
    nums.sort((a,b)=>{
           if(a>b)
             return -1;
           if(a<b)
               return 1;
            return 0;
    });
    return nums[2];
    
};