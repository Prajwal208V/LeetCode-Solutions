1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val, prev, next, child):
5        self.val = val
6        self.prev = prev
7        self.next = next
8        self.child = child
9"""
10
11from typing import Optional
12
13class Node:
14    def __init__(self, val, prev=None, next=None, child=None):
15        self.val = val
16        self.prev = prev
17        self.next = next
18        self.child = child
19
20class Solution:
21    def flatten(self, head: Optional[Node]) -> Optional[Node]:
22        if not head:
23            return head
24
25        dummy = Node(0)
26        prev = dummy
27        stack = [head]
28
29        while stack:
30            curr = stack.pop()
31
32            prev.next = curr
33            curr.prev = prev
34
35            if curr.next:
36                stack.append(curr.next)
37            if curr.child:
38                stack.append(curr.child)
39                curr.child = None
40
41            prev = curr
42
43        dummy.next.prev = None
44        return dummy.next