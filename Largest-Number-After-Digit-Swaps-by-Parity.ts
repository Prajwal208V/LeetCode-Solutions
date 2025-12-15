1function largestInteger(num: number): number {
2    const digits = num.toString().split('').map(Number);
3    const even: number[] = [];
4    const odd: number[] = [];
5
6    for (const d of digits) {
7        (d % 2 === 0 ? even : odd).push(d);
8    }
9
10    even.sort((a, b) => b - a);
11    odd.sort((a, b) => b - a);
12
13    let e = 0, o = 0;
14    for (let i = 0; i < digits.length; i++) {
15        digits[i] = digits[i] % 2 === 0 ? even[e++] : odd[o++];
16    }
17
18    return Number(digits.join(''));
19}