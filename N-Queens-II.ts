1function totalNQueens(n: number): number {
2    let count = 0;
3
4    const cols = new Set<number>();
5    const diag1 = new Set<number>(); // row - col
6    const diag2 = new Set<number>(); // row + col
7
8    function backtrack(row: number): void {
9        if (row === n) {
10            count++;
11            return;
12        }
13
14        for (let col = 0; col < n; col++) {
15            if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) {
16                continue;
17            }
18
19            cols.add(col);
20            diag1.add(row - col);
21            diag2.add(row + col);
22
23            backtrack(row + 1);
24
25            cols.delete(col);
26            diag1.delete(row - col);
27            diag2.delete(row + col);
28        }
29    }
30
31    backtrack(0);
32    return count;
33}