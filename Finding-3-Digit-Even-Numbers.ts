1function findEvenNumbers(digits: number[]): number[] {
2    const res = new Set<number>();
3
4    for (let i = 0; i < digits.length; i++) {
5        for (let j = 0; j < digits.length; j++) {
6            for (let k = 0; k < digits.length; k++) {
7                if (i !== j && j !== k && i !== k) {
8                    if (digits[i] !== 0 && digits[k] % 2 === 0) {
9                        res.add(digits[i] * 100 + digits[j] * 10 + digits[k]);
10                    }
11                }
12            }
13        }
14    }
15    return Array.from(res).sort((a, b) => a - b);
16}