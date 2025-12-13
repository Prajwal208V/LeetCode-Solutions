1function slowestKey(releaseTimes: number[], keysPressed: string): string {
2    let maxDuration = releaseTimes[0];
3    let res = keysPressed[0];
4
5    for (let i = 1; i < releaseTimes.length; i++) {
6        const duration = releaseTimes[i] - releaseTimes[i - 1];
7        const key = keysPressed[i];
8
9        if (duration > maxDuration || 
10           (duration === maxDuration && key > res)) {
11            maxDuration = duration;
12            res = key;
13        }
14    }
15
16    return res;
17}