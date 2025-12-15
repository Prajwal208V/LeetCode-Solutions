1function timeRequiredToBuy(tickets: number[], k: number): number {
2    let time = 0;
3
4    for (let i = 0; i < tickets.length; i++) {
5        time += Math.min(tickets[i], tickets[k] - (i > k ? 1 : 0));
6    }
7
8    return time;
9}