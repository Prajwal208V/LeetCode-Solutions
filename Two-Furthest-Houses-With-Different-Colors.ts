1function maxDistance(colors: number[]): number {
2    let res = 0;
3    for (let i = 0; i < colors.length; i++) {
4        for (let j = colors.length - 1; j > i; j--) {
5            if (colors[i] !== colors[j]) {
6                res = Math.max(res, j - i);
7                break;
8            }
9        }
10    }
11    return res;
12}