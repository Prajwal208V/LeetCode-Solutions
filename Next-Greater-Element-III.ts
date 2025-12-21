1function nextGreaterElement(n: number): number {
2    const arr = n.toString().split('');
3    let i = arr.length - 2;
4    while (i >= 0 && arr[i] >= arr[i + 1]) i--;
5    if (i < 0) return -1;
6
7    let j = arr.length - 1;
8    while (arr[j] <= arr[i]) j--;
9    [arr[i], arr[j]] = [arr[j], arr[i]];
10    const res = parseInt(arr.slice(0, i + 1).concat(arr.slice(i + 1).reverse()).join(''));
11    return res > 2 ** 31 - 1 ? -1 : res;
12}