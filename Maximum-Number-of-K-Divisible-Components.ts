1function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
2  const graph: number[][] = Array.from({ length: n }, () => [])
3  for (const [u, v] of edges) {
4    graph[u].push(v)
5    graph[v].push(u)
6  }
7  let ans = 0
8  function dfs(u: number, p: number): number {
9    let sum = values[u]
10    for (const v of graph[u]) if (v !== p) sum += dfs(v, u)
11    if (sum % k === 0) ans++
12    return sum
13  }
14  dfs(0, -1)
15  return ans
16}
17