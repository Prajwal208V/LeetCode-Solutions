1function findSubarrays(nums: number[]): boolean {
2    const seen = new Set<number>()
3    for (let i = 0; i < nums.length - 1; i++) {
4        const s = nums[i] + nums[i + 1]
5        if (seen.has(s)) return true
6        seen.add(s)
7    }
8    return false
9}