1function addToArrayForm(num: number[], k: number): number[] {
2    let i = num.length - 1;
3    let carry = k;
4    const res: number[] = [];
5
6    while (i >= 0 || carry > 0) {
7        const sum = (i >= 0 ? num[i] : 0) + (carry % 10);
8        res.push(sum % 10);
9        carry = Math.floor(carry / 10) + Math.floor(sum / 10);
10        i--;
11    }
12
13    return res.reverse();
14}
15