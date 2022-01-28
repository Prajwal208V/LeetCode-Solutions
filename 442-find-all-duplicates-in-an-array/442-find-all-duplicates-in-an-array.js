/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let arr=[];
    nums.sort((a,b)=>{
        if(a>b)
            return 1;
        if(a<b)
            return -1;
        return 0;
    })
    for(let i=0;i<nums.length;i++){
        if(nums[i]===nums[i+1])
            arr.push(nums[i]);
    }
    return arr;
};