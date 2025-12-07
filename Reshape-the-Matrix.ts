1function matrixReshape(mat: number[][], r: number, c: number): number[][] {
2    const m = mat.length;
3    const n = mat[0].length;
4    if (m * n !== r * c) return mat;
5
6    const res: number[][] = Array.from({ length: r }, () => Array(c).fill(0));
7    let idx = 0;
8
9    for (let i = 0; i < m; i++) {
10        for (let j = 0; j < n; j++) {
11            const nr = Math.floor(idx / c);
12            const nc = idx % c;
13            res[nr][nc] = mat[i][j];
14            idx++;
15        }
16    }
17    return res;
18}
19