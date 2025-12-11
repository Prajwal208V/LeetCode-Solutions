1class LRUCache {
2  private cap: number
3  private map: Map<number, number>
4  constructor(capacity: number) {
5    this.cap = capacity
6    this.map = new Map()
7  }
8  get(key: number): number {
9    if (!this.map.has(key)) return -1
10    const val = this.map.get(key)!
11    this.map.delete(key)
12    this.map.set(key, val)
13    return val
14  }
15  put(key: number, value: number): void {
16    if (this.map.has(key)) this.map.delete(key)
17    this.map.set(key, value)
18    if (this.map.size > this.cap) {
19      const firstKey = this.map.keys().next().value
20      this.map.delete(firstKey)
21    }
22  }
23}
24
25/**
26 * Your LRUCache object will be instantiated and called as such:
27 * var obj = new LRUCache(capacity)
28 * var param_1 = obj.get(key)
29 * obj.put(key,value)
30 */