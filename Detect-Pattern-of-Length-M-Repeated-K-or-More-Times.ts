1function containsPattern(arr: number[], m: number, k: number): boolean {
2    let count = 0;
3
4    for (let i = 0; i + m < arr.length; i++) {
5        if (arr[i] === arr[i + m]) {
6            count++;
7            if (count === m * (k - 1)) return true;
8        } else {
9            count = 0;
10        }
11    }
12
13    return false;
14}