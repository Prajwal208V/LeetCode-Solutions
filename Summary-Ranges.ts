1function summaryRanges(nums: number[]): string[] {
2    const res: string[] = [];
3    let i = 0;
4
5    while (i < nums.length) {
6        let start = nums[i];
7        while (i + 1 < nums.length && nums[i + 1] === nums[i] + 1) {
8            i++;
9        }
10        if (start === nums[i]) res.push(start.toString());
11        else res.push(start + "->" + nums[i]);
12        i++;
13    }
14
15    return res;
16}
17