1function subsetsWithDup(nums: number[]): number[][] {
2    nums.sort((a, b) => a - b);
3    const res: number[][] = [[]];
4    let start = 0;
5
6    for (let i = 0; i < nums.length; i++) {
7        const size = res.length;
8        let j = i > 0 && nums[i] === nums[i - 1] ? start : 0;
9        start = size;
10        for (; j < size; j++) {
11            res.push([...res[j], nums[i]]);
12        }
13    }
14
15    return res;
16}
17