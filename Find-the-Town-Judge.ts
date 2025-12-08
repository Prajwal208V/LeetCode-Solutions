1function findJudge(n: number, trust: number[][]): number {
2    const score = new Array(n + 1).fill(0);
3
4    for (const [a, b] of trust) {
5        score[a]--;
6        score[b]++;
7    }
8
9    for (let i = 1; i <= n; i++) {
10        if (score[i] === n - 1) return i;
11    }
12
13    return -1;
14}