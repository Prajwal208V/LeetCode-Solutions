1/** 
2 * Forward declaration of guess API.
3 * @param {number} num   your guess
4 * @return 	     -1 if num is higher than the picked number
5 *			      1 if num is lower than the picked number
6 *               otherwise return 0
7 * var guess = function(num) {}
8 */
9
10
11function guessNumber(n: number): number {
12    let l = 1, r = n;
13    while (l <= r) {
14        const m = Math.floor((l + r) / 2);
15        const res = guess(m);
16        if (res === 0) return m;
17        if (res < 0) r = m - 1;
18        else l = m + 1;
19    }
20    return -1;
21}
22