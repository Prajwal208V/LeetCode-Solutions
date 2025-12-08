1function validMountainArray(arr: number[]): boolean {
2    const n = arr.length;
3    let i = 0;
4
5    while (i + 1 < n && arr[i] < arr[i + 1]) i++;
6
7    if (i === 0 || i === n - 1) return false;
8
9    while (i + 1 < n && arr[i] > arr[i + 1]) i++;
10
11    return i === n - 1;
12}
13