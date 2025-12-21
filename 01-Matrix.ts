1function updateMatrix(mat: number[][]): number[][] {
2    const m = mat.length, n = mat[0].length;
3    const q: [number, number][] = [];
4    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
5
6    for (let i = 0; i < m; i++)
7        for (let j = 0; j < n; j++)
8            mat[i][j] === 0 ? q.push([i, j]) : mat[i][j] = Infinity;
9
10    for (let [r, c] of q)
11        for (let [dr, dc] of dirs) {
12            const nr = r + dr, nc = c + dc;
13            if (nr >= 0 && nc >= 0 && nr < m && nc < n && mat[nr][nc] > mat[r][c] + 1) {
14                mat[nr][nc] = mat[r][c] + 1;
15                q.push([nr, nc]);
16            }
17        }
18    return mat;
19}