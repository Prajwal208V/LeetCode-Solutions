/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    let past_arr=nums.filter((a)=> a>=0);
    let negt_arr=nums.filter((a)=> a<0);
    let res_arr=[];
    for(let i=0;i<past_arr.length;i++){
        res_arr.push(past_arr[i]);
        res_arr.push(negt_arr[i]);
    }
    return res_arr;
    
};