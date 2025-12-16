1function countAsterisks(s: string): number {
2    let count = 0;
3    let inside = false;
4
5    for (const c of s) {
6        if (c === '|') inside = !inside;
7        else if (c === '*' && !inside) count++;
8    }
9    return count;
10}