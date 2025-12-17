1function updateBoard(board: string[][], click: number[]): string[][] {
2    const [r, c] = click
3    if (board[r][c] === 'M') {
4        board[r][c] = 'X'
5        return board
6    }
7
8    const dirs = [-1, 0, 1]
9    const dfs = (x: number, y: number) => {
10        let mines = 0
11        for (const dx of dirs)
12            for (const dy of dirs) {
13                const nx = x + dx, ny = y + dy
14                if (nx >= 0 && ny >= 0 && nx < board.length && ny < board[0].length) {
15                    if (board[nx][ny] === 'M') mines++
16                }
17            }
18
19        if (mines > 0) {
20            board[x][y] = mines.toString()
21            return
22        }
23
24        board[x][y] = 'B'
25        for (const dx of dirs)
26            for (const dy of dirs) {
27                const nx = x + dx, ny = y + dy
28                if (
29                    nx >= 0 && ny >= 0 &&
30                    nx < board.length && ny < board[0].length &&
31                    board[nx][ny] === 'E'
32                ) {
33                    dfs(nx, ny)
34                }
35            }
36    }
37
38    dfs(r, c)
39    return board
40}