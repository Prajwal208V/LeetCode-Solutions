1function numSub(s: string): number {
2  const MOD = 1000000007
3  let res = 0
4  let cnt = 0
5  for (let i = 0; i < s.length; i++) {
6    if (s[i] === '1') cnt++
7    else {
8      res = (res + (cnt * (cnt + 1) / 2) % MOD) % MOD
9      cnt = 0
10    }
11  }
12  res = (res + (cnt * (cnt + 1) / 2) % MOD) % MOD
13  return res
14}
15