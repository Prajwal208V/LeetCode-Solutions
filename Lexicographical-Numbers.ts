1function lexicalOrder(n: number): number[] {
2  const res: number[] = [];
3  let cur = 1;
4  for (let i = 0; i < n; i++) {
5    res.push(cur);
6    if (cur * 10 <= n) {
7      cur *= 10;
8    } else {
9      if (cur >= n) cur = Math.floor(cur / 10);
10      cur++;
11      while (cur % 10 === 0) {
12        cur = Math.floor(cur / 10);
13      }
14    }
15  }
16  return res;
17}
18