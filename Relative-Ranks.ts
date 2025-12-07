1function findRelativeRanks(score: number[]): string[] {
2    const n = score.length;
3    const idx = score.map((_, i) => i);
4    idx.sort((a, b) => score[b] - score[a]);
5
6    const res: string[] = Array(n);
7    for (let i = 0; i < n; i++) {
8        const pos = idx[i];
9        if (i === 0) res[pos] = "Gold Medal";
10        else if (i === 1) res[pos] = "Silver Medal";
11        else if (i === 2) res[pos] = "Bronze Medal";
12        else res[pos] = (i + 1).toString();
13    }
14    return res;
15}
16