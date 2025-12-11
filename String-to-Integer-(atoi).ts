1function myAtoi(s: string): number {
2  let i = 0
3  const n = s.length
4
5  while (i < n && s[i] === ' ') i++
6
7  let sign = 1
8  if (i < n && (s[i] === '+' || s[i] === '-')) {
9    sign = s[i] === '-' ? -1 : 1
10    i++
11  }
12
13  let num = 0
14  const INT_MAX = 2147483647
15  const INT_MIN = -2147483648
16
17  while (i < n && s[i] >= '0' && s[i] <= '9') {
18    const digit = s.charCodeAt(i) - 48
19
20    if (num > Math.floor(INT_MAX / 10) || 
21       (num === Math.floor(INT_MAX / 10) && digit > INT_MAX % 10)) {
22      return sign === 1 ? INT_MAX : INT_MIN
23    }
24
25    num = num * 10 + digit
26    i++
27  }
28
29  return num * sign
30}