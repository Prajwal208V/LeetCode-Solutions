1function divisorSubstrings(num: number, k: number): number {
2    const s = num.toString();
3    let count = 0;
4
5    for (let i = 0; i <= s.length - k; i++) {
6        const val = Number(s.slice(i, i + k));
7        if (val !== 0 && num % val === 0) count++;
8    }
9    return count;
10};