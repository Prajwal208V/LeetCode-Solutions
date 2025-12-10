1/**
2 Do not return anything, modify matrix in-place instead.
3 */
4function setZeroes(matrix: number[][]): void {
5    const m = matrix.length;
6    const n = matrix[0].length;
7    let firstRowZero = false;
8    let firstColZero = false;
9
10    for (let j = 0; j < n; j++) {
11        if (matrix[0][j] === 0) {
12            firstRowZero = true;
13            break;
14        }
15    }
16
17    for (let i = 0; i < m; i++) {
18        if (matrix[i][0] === 0) {
19            firstColZero = true;
20            break;
21        }
22    }
23
24    for (let i = 1; i < m; i++) {
25        for (let j = 1; j < n; j++) {
26            if (matrix[i][j] === 0) {
27                matrix[i][0] = 0;
28                matrix[0][j] = 0;
29            }
30        }
31    }
32
33    for (let i = 1; i < m; i++) {
34        if (matrix[i][0] === 0) {
35            for (let j = 1; j < n; j++) {
36                matrix[i][j] = 0;
37            }
38        }
39    }
40
41    for (let j = 1; j < n; j++) {
42        if (matrix[0][j] === 0) {
43            for (let i = 1; i < m; i++) {
44                matrix[i][j] = 0;
45            }
46        }
47    }
48
49    if (firstRowZero) {
50        for (let j = 0; j < n; j++) {
51            matrix[0][j] = 0;
52        }
53    }
54
55    if (firstColZero) {
56        for (let i = 0; i < m; i++) {
57            matrix[i][0] = 0;
58        }
59    }
60}
61