1function countCoveredBuildings(n: number, buildings: number[][]): number {
2  const rows = new Map<number, number[]>()
3  const cols = new Map<number, number[]>()
4  for (const [x, y] of buildings) {
5    if (!rows.has(x)) rows.set(x, [])
6    if (!cols.has(y)) cols.set(y, [])
7    rows.get(x)!.push(y)
8    cols.get(y)!.push(x)
9  }
10  for (const arr of rows.values()) arr.sort((a, b) => a - b)
11  for (const arr of cols.values()) arr.sort((a, b) => a - b)
12  let ans = 0
13  for (const [x, y] of buildings) {
14    const r = rows.get(x)!
15    const c = cols.get(y)!
16    if (r[0] < y && y < r[r.length - 1] && c[0] < x && x < c[c.length - 1]) ans++
17  }
18  return ans
19}