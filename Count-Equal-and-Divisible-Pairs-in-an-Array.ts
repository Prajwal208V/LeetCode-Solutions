1function countPairs(nums: number[], k: number): number {
2    let count = 0;
3    for (let i = 0; i < nums.length; i++) {
4        for (let j = i + 1; j < nums.length; j++) {
5            if (nums[i] === nums[j] && (i * j) % k === 0) count++;
6        }
7    }
8    return count;
9}