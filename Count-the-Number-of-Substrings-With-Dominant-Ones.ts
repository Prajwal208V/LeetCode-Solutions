1function numberOfSubstrings(s: string): number {
2  const n = s.length
3  let ans = 0
4  const maxZero = Math.floor((-1 + Math.sqrt(1 + 4 * n)) / 2)
5  for (let zero = 0; zero <= maxZero; zero++) {
6    let lastInvalid = -1
7    let cnt0 = 0
8    let cnt1 = 0
9    let l = 0
10    for (let r = 0; r < n; r++) {
11      if (s[r] === '0') cnt0++
12      else cnt1++
13      while (l < r) {
14        if (s[l] === '0' && cnt0 > zero) {
15          cnt0--
16          lastInvalid = l
17          l++
18        } else if (s[l] === '1' && cnt1 - 1 >= zero * zero) {
19          cnt1--
20          l++
21        } else break
22      }
23      if (cnt0 === zero && cnt1 >= zero * zero) ans += l - lastInvalid
24    }
25  }
26  return ans
27}