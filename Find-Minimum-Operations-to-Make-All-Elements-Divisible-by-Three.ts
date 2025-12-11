1function minimumOperations(nums: number[]): number {
2  let cnt = 0
3  for (const x of nums) if (x % 3 !== 0) cnt++
4  return cnt
5}
6