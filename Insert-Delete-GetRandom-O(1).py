1import random
2from typing import Dict, List
3
4class RandomizedSet:
5    def __init__(self):
6        self.idx: Dict[int, int] = {}
7        self.arr: List[int] = []
8
9    def insert(self, val: int) -> bool:
10        if val in self.idx:
11            return False
12        self.idx[val] = len(self.arr)
13        self.arr.append(val)
14        return True
15
16    def remove(self, val: int) -> bool:
17        if val not in self.idx:
18            return False
19        i = self.idx[val]
20        last = self.arr[-1]
21        self.arr[i] = last
22        self.idx[last] = i
23        self.arr.pop()
24        del self.idx[val]
25        return True
26
27    def getRandom(self) -> int:
28        return random.choice(self.arr)
29
30