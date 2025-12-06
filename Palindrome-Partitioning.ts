1function partition(s: string): string[][] {
2    const n = s.length;
3    const isPal: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
4    for (let len = 1; len <= n; len++) {
5        for (let i = 0; i + len - 1 < n; i++) {
6            const j = i + len - 1;
7            if (s[i] === s[j] && (len <= 2 || isPal[i + 1][j - 1])) {
8                isPal[i][j] = true;
9            }
10        }
11    }
12    const res: string[][] = [];
13    const cur: string[] = [];
14    function dfs(start: number) {
15        if (start === n) {
16            res.push(cur.slice());
17            return;
18        }
19        for (let end = start; end < n; end++) {
20            if (isPal[start][end]) {
21                cur.push(s.substring(start, end + 1));
22                dfs(end + 1);
23                cur.pop();
24            }
25        }
26    }
27    dfs(0);
28    return res;
29}
30