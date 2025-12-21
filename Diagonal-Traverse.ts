1function findDiagonalOrder(mat: number[][]): number[] {
2    if (!mat.length) return [];
3    const m = mat.length, n = mat[0].length;
4    const res: number[] = [];
5    let r = 0, c = 0, dir = 1; // dir=1 up-right, -1 down-left
6    for (let i = 0; i < m * n; i++) {
7        res.push(mat[r][c]);
8        if (dir === 1) {
9            if (c === n - 1) { r++; dir = -1; }
10            else if (r === 0) { c++; dir = -1; }
11            else { r--; c++; }
12        } else {
13            if (r === m - 1) { c++; dir = 1; }
14            else if (c === 0) { r++; dir = 1; }
15            else { r++; c--; }
16        }
17    }
18    return res;
19}