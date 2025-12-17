1function countDaysTogether(
2    arriveAlice: string,
3    leaveAlice: string,
4    arriveBob: string,
5    leaveBob: string
6): number {
7    const days = [31,28,31,30,31,30,31,31,30,31,30,31]
8
9    const toDay = (date: string): number => {
10        const [m, d] = date.split("-").map(Number)
11        let total = d
12        for (let i = 0; i < m - 1; i++) total += days[i]
13        return total
14    }
15
16    const a1 = toDay(arriveAlice)
17    const a2 = toDay(leaveAlice)
18    const b1 = toDay(arriveBob)
19    const b2 = toDay(leaveBob)
20
21    const start = Math.max(a1, b1)
22    const end = Math.min(a2, b2)
23
24    return Math.max(0, end - start + 1)
25}