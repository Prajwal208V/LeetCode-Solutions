1function prefixesDivBy5(nums: number[]): boolean[] {
2    const res: boolean[] = [];
3    let cur = 0;
4
5    for (const bit of nums) {
6        cur = (cur * 2 + bit) % 5;
7        res.push(cur === 0);
8    }
9
10    return res;
11}
12