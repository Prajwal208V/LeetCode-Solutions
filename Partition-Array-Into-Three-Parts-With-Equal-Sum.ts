1function canThreePartsEqualSum(arr: number[]): boolean {
2    const total = arr.reduce((a, b) => a + b, 0);
3    if (total % 3 !== 0) return false;
4    const target = total / 3;
5    let sum = 0;
6    let count = 0;
7    for (let i = 0; i < arr.length; i++) {
8        sum += arr[i];
9        if (sum === target) {
10            count++;
11            sum = 0;
12        }
13    }
14    return count >= 3;
15}
16