/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let result_arr=nums.map((a)=> a*a).sort((a,b)=>{
        if(a<b)
            return -1
        if(a>b)
            return 1;
        return 0;
    })
    return result_arr;
};