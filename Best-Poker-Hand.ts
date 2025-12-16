1function bestHand(ranks: number[], suits: string[]): string {
2    const sameSuit = suits.every(s => s === suits[0]);
3    if (sameSuit) return "Flush";
4
5    const freq = new Map<number, number>();
6    for (const r of ranks) freq.set(r, (freq.get(r) || 0) + 1);
7
8    let maxCount = 0;
9    for (const c of freq.values()) maxCount = Math.max(maxCount, c);
10
11    if (maxCount >= 3) return "Three of a Kind";
12    if (maxCount === 2) return "Pair";
13    return "High Card";
14}