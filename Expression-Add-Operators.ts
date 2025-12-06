1function addOperators(num: string, target: number): string[] {
2    const res: string[] = [];
3    const n = num.length;
4
5    function dfs(i: number, path: string, evalVal: number, last: number) {
6        if (i === n) {
7            if (evalVal === target) res.push(path);
8            return;
9        }
10        for (let j = i; j < n; j++) {
11            if (j > i && num[i] === '0') break;
12            const curStr = num.slice(i, j + 1);
13            const cur = Number(curStr);
14            if (i === 0) {
15                dfs(j + 1, curStr, cur, cur);
16            } else {
17                dfs(j + 1, path + '+' + curStr, evalVal + cur, cur);
18                dfs(j + 1, path + '-' + curStr, evalVal - cur, -cur);
19                dfs(j + 1, path + '*' + curStr, evalVal - last + last * cur, last * cur);
20            }
21        }
22    }
23
24    dfs(0, '', 0, 0);
25    return res;
26}
27