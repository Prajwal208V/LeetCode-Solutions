1function convertToBase7(num: number): string {
2    if (num === 0) return "0";
3    const sign = num < 0 ? -1 : 1;
4    num = Math.abs(num);
5    let res = "";
6    while (num > 0) {
7        res = (num % 7).toString() + res;
8        num = Math.floor(num / 7);
9    }
10    return sign < 0 ? "-" + res : res;
11}
12