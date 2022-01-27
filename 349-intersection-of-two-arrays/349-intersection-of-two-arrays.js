/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let set1=new Set(nums1);
    let set2=new Set(nums2);
    nums1=[...set1];
    nums2=[...set2];
    let result_arr=[];
    for(let i of nums1){
        if(nums2.includes(i))
            result_arr.push(i);
    }
    return result_arr;
};