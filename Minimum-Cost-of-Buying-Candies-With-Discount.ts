1function minimumCost(cost: number[]): number {
2    cost.sort((a, b) => b - a);
3    let sum = 0;
4
5    for (let i = 0; i < cost.length; i++) {
6        if ((i + 1) % 3 !== 0) sum += cost[i];
7    }
8    return sum;
9}