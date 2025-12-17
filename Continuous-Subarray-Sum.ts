1function checkSubarraySum(nums: number[], k: number): boolean {
2    const map = new Map<number, number>()
3    map.set(0, -1)
4    let sum = 0
5
6    for (let i = 0; i < nums.length; i++) {
7        sum += nums[i]
8        if (k !== 0) sum %= k
9        if (map.has(sum)) {
10            if (i - map.get(sum)! > 1) return true
11        } else {
12            map.set(sum, i)
13        }
14    }
15    return false
16}