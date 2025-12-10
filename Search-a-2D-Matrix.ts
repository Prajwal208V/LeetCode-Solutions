1function searchMatrix(matrix: number[][], target: number): boolean {
2    const m = matrix.length;
3    const n = matrix[0].length;
4    let left = 0;
5    let right = m * n - 1;
6
7    while (left <= right) {
8        const mid = left + ((right - left) >> 1);
9        const row = Math.floor(mid / n);
10        const col = mid % n;
11        const val = matrix[row][col];
12
13        if (val === target) return true;
14        if (val < target) left = mid + 1;
15        else right = mid - 1;
16    }
17
18    return false;
19}