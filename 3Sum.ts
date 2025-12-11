1function threeSum(nums: number[]): number[][] {
2    nums.sort((a, b) => a - b);
3    const res: number[][] = [];
4    const n = nums.length;
5
6    for (let i = 0; i < n - 2; i++) {
7        if (i > 0 && nums[i] === nums[i - 1]) continue;
8        let l = i + 1;
9        let r = n - 1;
10        while (l < r) {
11            const sum = nums[i] + nums[l] + nums[r];
12            if (sum === 0) {
13                res.push([nums[i], nums[l], nums[r]]);
14                l++;
15                r--;
16                while (l < r && nums[l] === nums[l - 1]) l++;
17                while (l < r && nums[r] === nums[r + 1]) r--;
18            } else if (sum < 0) {
19                l++;
20            } else {
21                r--;
22            }
23        }
24    }
25    return res;
26}