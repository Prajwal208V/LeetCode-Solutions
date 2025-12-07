1function reverseStr(s: string, k: number): string {
2    const arr = s.split('');
3    for (let i = 0; i < arr.length; i += 2 * k) {
4        let l = i;
5        let r = Math.min(i + k - 1, arr.length - 1);
6        while (l < r) {
7            [arr[l], arr[r]] = [arr[r], arr[l]];
8            l++;
9            r--;
10        }
11    }
12    return arr.join('');
13}
14