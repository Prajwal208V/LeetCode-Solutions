1function canCompleteCircuit(gas: number[], cost: number[]): number {
2  let total = 0
3  let tank = 0
4  let start = 0
5
6  for (let i = 0; i < gas.length; i++) {
7    const diff = gas[i] - cost[i]
8    total += diff
9    tank += diff
10
11    if (tank < 0) {
12      start = i + 1
13      tank = 0
14    }
15  }
16
17  return total >= 0 ? start : -1
18}