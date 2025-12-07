1function validPalindrome(s: string): boolean {
2    function isPal(i: number, j: number): boolean {
3        while (i < j) {
4            if (s[i] !== s[j]) return false;
5            i++;
6            j--;
7        }
8        return true;
9    }
10
11    let l = 0, r = s.length - 1;
12    while (l < r) {
13        if (s[l] !== s[r]) {
14            return isPal(l + 1, r) || isPal(l, r - 1);
15        }
16        l++;
17        r--;
18    }
19    return true;
20}
21