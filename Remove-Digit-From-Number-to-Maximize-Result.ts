1function removeDigit(number: string, digit: string): string {
2    let res = "0";
3
4    for (let i = 0; i < number.length; i++) {
5        if (number[i] === digit) {
6            const candidate = number.slice(0, i) + number.slice(i + 1);
7            if (candidate > res) res = candidate;
8        }
9    }
10    return res;
11}