1from typing import List
2
3class OrderedStream:
4
5    def __init__(self, n: int):
6        self.stream = [""] * (n + 1)
7        self.ptr = 1
8
9    def insert(self, idKey: int, value: str) -> List[str]:
10        self.stream[idKey] = value
11        res = []
12        
13        while self.ptr < len(self.stream) and self.stream[self.ptr] != "":
14            res.append(self.stream[self.ptr])
15            self.ptr += 1
16        
17        return res
18
19
20# Your OrderedStream object will be instantiated and called as such:
21# obj = OrderedStream(n)
22# param_1 = obj.insert(idKey,value)