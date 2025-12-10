1function combinationSum2(candidates: number[], target: number): number[][] {
2    candidates.sort((a, b) => a - b);
3    const res: number[][] = [];
4    const path: number[] = [];
5
6    function backtrack(start: number, remain: number): void {
7        if (remain === 0) {
8            res.push([...path]);
9            return;
10        }
11        if (remain < 0) return;
12
13        for (let i = start; i < candidates.length; i++) {
14            if (i > start && candidates[i] === candidates[i - 1]) continue;
15            const val = candidates[i];
16            if (val > remain) break;
17            path.push(val);
18            backtrack(i + 1, remain - val);
19            path.pop();
20        }
21    }
22
23    backtrack(0, target);
24    return res;
25}