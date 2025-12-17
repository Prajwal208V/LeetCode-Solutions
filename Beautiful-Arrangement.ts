1function countArrangement(n: number): number {
2    const used = new Array(n + 1).fill(false)
3    let count = 0
4
5    const backtrack = (pos: number) => {
6        if (pos > n) {
7            count++
8            return
9        }
10        for (let i = 1; i <= n; i++) {
11            if (!used[i] && (i % pos === 0 || pos % i === 0)) {
12                used[i] = true
13                backtrack(pos + 1)
14                used[i] = false
15            }
16        }
17    }
18
19    backtrack(1)
20    return count
21}