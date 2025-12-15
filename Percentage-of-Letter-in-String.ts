1function percentageLetter(s: string, letter: string): number {
2    let count = 0;
3    for (const c of s) {
4        if (c === letter) count++;
5    }
6    return Math.floor((count * 100) / s.length);
7}