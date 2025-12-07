1function checkPerfectNumber(num: number): boolean {
2    if (num <= 1) return false;
3    let sum = 1;
4    const limit = Math.floor(Math.sqrt(num));
5    for (let i = 2; i <= limit; i++) {
6        if (num % i === 0) {
7            sum += i;
8            const d = num / i;
9            if (d !== i) sum += d;
10        }
11    }
12    return sum === num;
13}
14