1function countElements(nums: number[]): number {
2    const min = Math.min(...nums);
3    const max = Math.max(...nums);
4    return nums.filter(n => n > min && n < max).length;
5}