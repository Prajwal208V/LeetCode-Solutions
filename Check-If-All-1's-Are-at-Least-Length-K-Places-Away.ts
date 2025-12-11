1function kLengthApart(nums: number[], k: number): boolean {
2  let prev = -1_000_000_000
3  for (let i = 0; i < nums.length; i++) {
4    if (nums[i] === 1) {
5      if (i - prev - 1 < k) return false
6      prev = i
7    }
8  }
9  return true
10}