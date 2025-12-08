1function numRookCaptures(board: string[][]): number {
2    let r = 0, c = 0;
3
4    for (let i = 0; i < 8; i++) {
5        for (let j = 0; j < 8; j++) {
6            if (board[i][j] === 'R') {
7                r = i;
8                c = j;
9            }
10        }
11    }
12
13    let ans = 0;
14    const dirs = [[1,0], [-1,0], [0,1], [0,-1]];
15
16    for (const [dr, dc] of dirs) {
17        let x = r + dr;
18        let y = c + dc;
19        while (x >= 0 && x < 8 && y >= 0 && y < 8) {
20            if (board[x][y] === 'B') break;
21            if (board[x][y] === 'p') {
22                ans++;
23                break;
24            }
25            x += dr;
26            y += dc;
27        }
28    }
29
30    return ans;
31}
32