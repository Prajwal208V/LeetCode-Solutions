1function digitSum(s: string, k: number): string {
2    while (s.length > k) {
3        let next = "";
4        for (let i = 0; i < s.length; i += k) {
5            let sum = 0;
6            for (const c of s.slice(i, i + k)) {
7                sum += Number(c);
8            }
9            next += sum.toString();
10        }
11        s = next;
12    }
13    return s;
14}