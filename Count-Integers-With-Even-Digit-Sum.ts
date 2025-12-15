1function countEven(num: number): number {
2    let count = 0;
3
4    for (let i = 1; i <= num; i++) {
5        let sum = 0;
6        let x = i;
7
8        while (x > 0) {
9            sum += x % 10;
10            x = Math.floor(x / 10);
11        }
12
13        if (sum % 2 === 0) count++;
14    }
15
16    return count;
17}