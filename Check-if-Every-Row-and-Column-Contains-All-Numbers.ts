1function checkValid(matrix: number[][]): boolean {
2    const n = matrix.length;
3
4    for (let i = 0; i < n; i++) {
5        const rowSet = new Set<number>();
6        const colSet = new Set<number>();
7
8        for (let j = 0; j < n; j++) {
9            rowSet.add(matrix[i][j]);
10            colSet.add(matrix[j][i]);
11        }
12
13        if (rowSet.size !== n || colSet.size !== n) {
14            return false;
15        }
16    }
17
18    return true;
19}