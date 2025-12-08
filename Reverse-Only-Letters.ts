1function reverseOnlyLetters(s: string): string {
2    const arr = s.split('');
3    let l = 0, r = arr.length - 1;
4
5    function isLetter(c: string): boolean {
6        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
7    }
8
9    while (l < r) {
10        if (!isLetter(arr[l])) {
11            l++;
12        } else if (!isLetter(arr[r])) {
13            r--;
14        } else {
15            [arr[l], arr[r]] = [arr[r], arr[l]];
16            l++;
17            r--;
18        }
19    }
20
21    return arr.join('');
22}