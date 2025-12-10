1function fourSum(nums: number[], target: number): number[][] {
2    nums.sort((a, b) => a - b);
3    const n = nums.length;
4    const res: number[][] = [];
5
6    for (let i = 0; i < n - 3; i++) {
7        if (i > 0 && nums[i] === nums[i - 1]) continue;
8        for (let j = i + 1; j < n - 2; j++) {
9            if (j > i + 1 && nums[j] === nums[j - 1]) continue;
10            let l = j + 1;
11            let r = n - 1;
12            while (l < r) {
13                const sum = nums[i] + nums[j] + nums[l] + nums[r];
14                if (sum === target) {
15                    res.push([nums[i], nums[j], nums[l], nums[r]]);
16                    l++;
17                    r--;
18                    while (l < r && nums[l] === nums[l - 1]) l++;
19                    while (l < r && nums[r] === nums[r + 1]) r--;
20                } else if (sum < target) {
21                    l++;
22                } else {
23                    r--;
24                }
25            }
26        }
27    }
28
29    return res;
30}
31