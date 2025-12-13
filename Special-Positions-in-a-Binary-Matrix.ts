1function numSpecial(mat: number[][]): number {
2    const m = mat.length;
3    const n = mat[0].length;
4
5    const rowCount = new Array(m).fill(0);
6    const colCount = new Array(n).fill(0);
7
8    for (let i = 0; i < m; i++) {
9        for (let j = 0; j < n; j++) {
10            if (mat[i][j] === 1) {
11                rowCount[i]++;
12                colCount[j]++;
13            }
14        }
15    }
16
17    let res = 0;
18    for (let i = 0; i < m; i++) {
19        for (let j = 0; j < n; j++) {
20            if (mat[i][j] === 1 && rowCount[i] === 1 && colCount[j] === 1) {
21                res++;
22            }
23        }
24    }
25
26    return res;
27}