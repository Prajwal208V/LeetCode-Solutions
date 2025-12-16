1function convertTime(current: string, correct: string): number {
2    const toMinutes = (time: string): number => {
3        const [h, m] = time.split(":").map(Number);
4        return h * 60 + m;
5    };
6
7    let diff = toMinutes(correct) - toMinutes(current);
8    let ops = 0;
9
10    const steps = [60, 15, 5, 1];
11
12    for (const step of steps) {
13        ops += Math.floor(diff / step);
14        diff %= step;
15    }
16
17    return ops;
18}