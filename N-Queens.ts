1function solveNQueens(n: number): string[][] {
2    const res: string[][] = [];
3    const board: string[] = new Array(n).fill("").map(() => ".".repeat(n));
4    const cols = new Set<number>();
5    const diag1 = new Set<number>();
6    const diag2 = new Set<number>();
7
8    function backtrack(r: number): void {
9        if (r === n) {
10            res.push([...board]);
11            return;
12        }
13        for (let c = 0; c < n; c++) {
14            if (cols.has(c) || diag1.has(r - c) || diag2.has(r + c)) continue;
15            cols.add(c);
16            diag1.add(r - c);
17            diag2.add(r + c);
18            const rowArr = board[r].split("");
19            rowArr[c] = "Q";
20            board[r] = rowArr.join("");
21            backtrack(r + 1);
22            rowArr[c] = ".";
23            board[r] = rowArr.join("");
24            cols.delete(c);
25            diag1.delete(r - c);
26            diag2.delete(r + c);
27        }
28    }
29
30    backtrack(0);
31    return res;
32}