1function findLUSlength(strs: string[]): number {
2    strs.sort((a, b) => b.length - a.length)
3
4    const isSub = (a: string, b: string): boolean => {
5        let i = 0
6        for (const c of b) if (i < a.length && a[i] === c) i++
7        return i === a.length
8    }
9
10    for (let i = 0; i < strs.length; i++) {
11        let ok = true
12        for (let j = 0; j < strs.length; j++) {
13            if (i !== j && isSub(strs[i], strs[j])) {
14                ok = false
15                break
16            }
17        }
18        if (ok) return strs[i].length
19    }
20    return -1
21}