1function leastBricks(wall: number[][]): number {
2    const map = new Map<number, number>();
3    for (const row of wall) {
4        let sum = 0;
5        for (let i = 0; i < row.length - 1; i++) {
6            sum += row[i];
7            map.set(sum, (map.get(sum) || 0) + 1);
8        }
9    }
10    return wall.length - Math.max(0, ...map.values());
11}