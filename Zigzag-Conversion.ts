1function convert(s: string, numRows: number): string {
2  if (numRows === 1) return s
3  const rows: string[] = Array.from({ length: Math.min(numRows, s.length) }, () => "")
4  let cur = 0
5  let down = true
6  for (const ch of s) {
7    rows[cur] += ch
8    if (cur === 0) down = true
9    else if (cur === numRows - 1) down = false
10    cur += down ? 1 : -1
11  }
12  return rows.join("")
13}