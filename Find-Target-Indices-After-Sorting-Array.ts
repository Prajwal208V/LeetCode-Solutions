1function targetIndices(nums: number[], target: number): number[] {
2    nums.sort((a, b) => a - b);
3    const res: number[] = [];
4
5    for (let i = 0; i < nums.length; i++) {
6        if (nums[i] === target) res.push(i);
7    }
8    return res;
9}