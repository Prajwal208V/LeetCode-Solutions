1function countOperations(num1: number, num2: number): number {
2    let count = 0;
3    while (num1 > 0 && num2 > 0) {
4        if (num1 >= num2) num1 -= num2;
5        else num2 -= num1;
6        count++;
7    }
8    return count;
9}