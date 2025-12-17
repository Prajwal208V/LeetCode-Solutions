1function checkDistances(s: string, distance: number[]): boolean {
2    const first = new Array(26).fill(-1)
3    for (let i = 0; i < s.length; i++) {
4        const idx = s.charCodeAt(i) - 97
5        if (first[idx] === -1) first[idx] = i
6        else if (i - first[idx] - 1 !== distance[idx]) return false
7    }
8    return true
9}