1function canJump(nums: number[]): boolean {
2    let goal = nums.length - 1;
3    for (let i = nums.length - 2; i >= 0; i--) {
4        if (i + nums[i] >= goal) {
5            goal = i;
6        }
7    }
8    return goal === 0;
9}
10