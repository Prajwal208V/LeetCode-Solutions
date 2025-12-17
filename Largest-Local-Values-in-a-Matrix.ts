1function largestLocal(grid: number[][]): number[][] {
2    const n = grid.length
3    const res: number[][] = []
4    for (let i = 0; i < n - 2; i++) {
5        const row: number[] = []
6        for (let j = 0; j < n - 2; j++) {
7            let max = 0
8            for (let x = i; x < i + 3; x++) {
9                for (let y = j; y < j + 3; y++) {
10                    max = Math.max(max, grid[x][y])
11                }
12            }
13            row.push(max)
14        }
15        res.push(row)
16    }
17    return res
18}