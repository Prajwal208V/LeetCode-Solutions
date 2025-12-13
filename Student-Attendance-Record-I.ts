1function checkRecord(s: string): boolean {
2    let absents = 0;
3    let lateStreak = 0;
4
5    for (const ch of s) {
6        if (ch === 'A') {
7            absents++;
8            lateStreak = 0;
9            if (absents > 1) return false;
10        } else if (ch === 'L') {
11            lateStreak++;
12            if (lateStreak >= 3) return false;
13        } else {
14            lateStreak = 0;
15        }
16    }
17
18    return true;
19}