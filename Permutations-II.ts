1function permuteUnique(nums: number[]): number[][] {
2    nums.sort((a, b) => a - b);
3    const res: number[][] = [];
4    const used: boolean[] = new Array(nums.length).fill(false);
5    const path: number[] = [];
6
7    function backtrack(): void {
8        if (path.length === nums.length) {
9            res.push([...path]);
10            return;
11        }
12        for (let i = 0; i < nums.length; i++) {
13            if (used[i]) continue;
14            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
15            used[i] = true;
16            path.push(nums[i]);
17            backtrack();
18            path.pop();
19            used[i] = false;
20        }
21    }
22
23    backtrack();
24    return res;
25}
26