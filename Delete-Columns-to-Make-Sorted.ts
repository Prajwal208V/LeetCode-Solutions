1function minDeletionSize(strs: string[]): number {
2    const m = strs.length;
3    const n = strs[0].length;
4    let ans = 0;
5
6    for (let j = 0; j < n; j++) {
7        for (let i = 1; i < m; i++) {
8            if (strs[i][j] < strs[i - 1][j]) {
9                ans++;
10                break;
11            }
12        }
13    }
14
15    return ans;
16}
17