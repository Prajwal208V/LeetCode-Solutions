1function sumOddLengthSubarrays(arr: number[]): number {
2    const n = arr.length;
3    let sum = 0;
4
5    for (let i = 0; i < n; i++) {
6        const totalSubarrays = (i + 1) * (n - i);
7        const oddCount = Math.floor((totalSubarrays + 1) / 2);
8        sum += arr[i] * oddCount;
9    }
10
11    return sum;
12}