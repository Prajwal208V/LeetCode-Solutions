1function mostFrequentEven(nums: number[]): number {
2    const freq = new Map<number, number>()
3
4    for (const n of nums) {
5        if (n % 2 === 0) {
6            freq.set(n, (freq.get(n) ?? 0) + 1)
7        }
8    }
9
10    let ans = -1
11    let maxCount = 0
12
13    for (const [num, count] of freq) {
14        if (count > maxCount || (count === maxCount && num < ans)) {
15            maxCount = count
16            ans = num
17        }
18    }
19
20    return ans
21}