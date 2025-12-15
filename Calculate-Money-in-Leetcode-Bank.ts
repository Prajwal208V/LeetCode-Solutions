1function totalMoney(n: number): number {
2    let total = 0;
3    let week = 0;
4    let day = 0;
5
6    for (let i = 0; i < n; i++) {
7        total += week + day + 1;
8        day++;
9
10        if (day === 7) {
11            day = 0;
12            week++;
13        }
14    }
15
16    return total;
17}