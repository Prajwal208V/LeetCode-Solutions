1function minimumMoves(s: string): number {
2    let moves = 0;
3
4    for (let i = 0; i < s.length; i++) {
5        if (s[i] === 'X') {
6            moves++;
7            i += 2;
8        }
9    }
10
11    return moves;
12}