1function answerQueries(nums: number[], queries: number[]): number[] {
2    nums.sort((a, b) => a - b)
3    const prefix: number[] = []
4    let sum = 0
5    for (const n of nums) {
6        sum += n
7        prefix.push(sum)
8    }
9
10    return queries.map(q => {
11        let l = 0, r = prefix.length
12        while (l < r) {
13            const m = (l + r) >> 1
14            if (prefix[m] <= q) l = m + 1
15            else r = m
16        }
17        return l
18    })
19}