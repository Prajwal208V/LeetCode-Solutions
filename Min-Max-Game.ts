1function minMaxGame(nums: number[]): number {
2    while (nums.length > 1) {
3        const next: number[] = []
4        for (let i = 0; i < nums.length; i += 2) {
5            next.push((i / 2) % 2 === 0 ? Math.min(nums[i], nums[i + 1]) : Math.max(nums[i], nums[i + 1]))
6        }
7        nums = next
8    }
9    return nums[0]
10}