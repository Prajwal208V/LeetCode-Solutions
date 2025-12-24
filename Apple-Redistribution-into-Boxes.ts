1function minimumBoxes(apple: number[], capacity: number[]): number {
2    let totalApples = apple.reduce((a, b) => a + b, 0);
3
4    capacity.sort((a, b) => b - a);
5
6    let usedBoxes = 0;
7    let stored = 0;
8
9    for (const cap of capacity) {
10        stored += cap;
11        usedBoxes++;
12        if (stored >= totalApples) {
13            return usedBoxes;
14        }
15    }
16
17    return usedBoxes;
18}