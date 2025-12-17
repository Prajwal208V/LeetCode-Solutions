1function minimumRecolors(blocks: string, k: number): number {
2    let whites = 0
3    for (let i = 0; i < k; i++) if (blocks[i] === 'W') whites++
4    let ans = whites
5    for (let i = k; i < blocks.length; i++) {
6        if (blocks[i] === 'W') whites++
7        if (blocks[i - k] === 'W') whites--
8        ans = Math.min(ans, whites)
9    }
10    return ans
11}