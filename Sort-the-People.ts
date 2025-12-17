1function sortPeople(names: string[], heights: number[]): string[] {
2    const arr: [string, number][] = []
3
4    for (let i = 0; i < names.length; i++) {
5        arr.push([names[i], heights[i]])
6    }
7
8    arr.sort((a, b) => b[1] - a[1])
9    return arr.map(x => x[0])
10}