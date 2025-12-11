1function findFinalValue(nums: number[], original: number): number {
2  const s = new Set(nums)
3  let val = original
4  while (s.has(val)) val *= 2
5  return val
6}
7