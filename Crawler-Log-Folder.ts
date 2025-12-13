1function minOperations(logs: string[]): number {
2    let depth = 0;
3
4    for (const log of logs) {
5        if (log === "../") {
6            if (depth > 0) depth--;
7        } else if (log !== "./") {
8            depth++;
9        }
10    }
11
12    return depth;
13}