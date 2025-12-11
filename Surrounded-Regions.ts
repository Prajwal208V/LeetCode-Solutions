1/**
2 Do not return anything, modify board in-place instead.
3 */
4function solve(board: string[][]): void {
5  const m = board.length
6  const n = board[0].length
7
8  const dfs = (r: number, c: number) => {
9    if (r < 0 || c < 0 || r >= m || c >= n || board[r][c] !== "O") return
10    board[r][c] = "#" 
11    dfs(r + 1, c)
12    dfs(r - 1, c)
13    dfs(r, c + 1)
14    dfs(r, c - 1)
15  }
16
17  for (let i = 0; i < m; i++) {
18    dfs(i, 0)
19    dfs(i, n - 1)
20  }
21  for (let j = 0; j < n; j++) {
22    dfs(0, j)
23    dfs(m - 1, j)
24  }
25
26  for (let i = 0; i < m; i++) {
27    for (let j = 0; j < n; j++) {
28      if (board[i][j] === "O") board[i][j] = "X"
29      else if (board[i][j] === "#") board[i][j] = "O"
30    }
31  }
32}