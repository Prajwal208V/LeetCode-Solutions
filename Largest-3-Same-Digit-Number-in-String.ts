1function largestGoodInteger(num: string): string {
2    let res = "";
3
4    for (let i = 0; i <= num.length - 3; i++) {
5        if (num[i] === num[i + 1] && num[i] === num[i + 2]) {
6            const curr = num.slice(i, i + 3);
7            if (curr > res) res = curr;
8        }
9    }
10    return res;
11}