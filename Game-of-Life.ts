1/**
2 Do not return anything, modify board in-place instead.
3 */
4function gameOfLife(board: number[][]): void {
5    const m = board.length;
6    const n = board[0].length;
7
8    const dirs = [
9        [1, 0], [-1, 0], [0, 1], [0, -1],
10        [1, 1], [1, -1], [-1, 1], [-1, -1]
11    ];
12
13    for (let i = 0; i < m; i++) {
14        for (let j = 0; j < n; j++) {
15            let live = 0;
16            for (const [dx, dy] of dirs) {
17                const x = i + dx;
18                const y = j + dy;
19                if (x >= 0 && x < m && y >= 0 && y < n) {
20                    live += board[x][y] & 1;
21                }
22            }
23            if ((board[i][j] & 1) === 1) {
24                if (live === 2 || live === 3) {
25                    board[i][j] |= 2;
26                }
27            } else {
28                if (live === 3) {
29                    board[i][j] |= 2;
30                }
31            }
32        }
33    }
34
35    for (let i = 0; i < m; i++) {
36        for (let j = 0; j < n; j++) {
37            board[i][j] >>= 1;
38        }
39    }
40}
41