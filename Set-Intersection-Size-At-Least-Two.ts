1function intersectionSizeTwo(intervals: number[][]): number {
2  intervals.sort((a, b) => a[1] - b[1] || b[0] - a[0])
3  let a = -1
4  let b = -1
5  let ans = 0
6  for (const [l, r] of intervals) {
7    const need =
8      (a < l ? 1 : 0) +
9      (b < l ? 1 : 0)
10    if (need === 2) {
11      ans += 2
12      b = r
13      a = r - 1
14    } else if (need === 1) {
15      ans++
16      if (a < l) a = b
17      b = r
18    }
19  }
20  return ans
21}
22