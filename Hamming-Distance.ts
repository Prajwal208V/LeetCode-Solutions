1function hammingDistance(x: number, y: number): number {
2    let v = x ^ y;
3    let cnt = 0;
4    while (v) {
5        v &= v - 1;
6        cnt++;
7    }
8    return cnt;
9}
10