1function findPeakElement(nums: number[]): number {
2  let l = 0
3  let r = nums.length - 1
4  while (l < r) {
5    const m = Math.floor((l + r) / 2)
6    if (nums[m] > nums[m + 1]) r = m
7    else l = m + 1
8  }
9  return l
10}