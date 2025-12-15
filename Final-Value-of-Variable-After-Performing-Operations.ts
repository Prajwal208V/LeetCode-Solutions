1function finalValueAfterOperations(operations: string[]): number {
2    let x = 0;
3
4    for (const op of operations) {
5        if (op.includes('+')) x++;
6        else x--;
7    }
8
9    return x;
10}