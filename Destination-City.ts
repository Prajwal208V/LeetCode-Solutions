1function destCity(paths: string[][]): string {
2    const starts = new Set<string>();
3
4    for (const [from, _] of paths) {
5        starts.add(from);
6    }
7
8    for (const [_, to] of paths) {
9        if (!starts.has(to)) {
10            return to;
11        }
12    }
13
14    return "";
15}