1function findMaxLength(nums: number[]): number {
2    const map = new Map<number, number>()
3    map.set(0, -1)
4    let sum = 0
5    let res = 0
6
7    for (let i = 0; i < nums.length; i++) {
8        sum += nums[i] === 0 ? -1 : 1
9        if (map.has(sum)) {
10            res = Math.max(res, i - map.get(sum)!)
11        } else {
12            map.set(sum, i)
13        }
14    }
15    return res
16}