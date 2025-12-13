1function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
2    let count = 0;
3
4    for (let i = 0; i < startTime.length; i++) {
5        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
6            count++;
7        }
8    }
9
10    return count;
11}