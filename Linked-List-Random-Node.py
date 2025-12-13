1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6import random
7from typing import Optional
8
9class ListNode:
10    def __init__(self, val=0, next=None):
11        self.val = val
12        self.next = next
13
14class Solution:
15    def __init__(self, head: Optional[ListNode]):
16        self.head = head
17
18    def getRandom(self) -> int:
19        res = None
20        cur = self.head
21        i = 1
22        while cur:
23            if random.randrange(i) == 0:
24                res = cur.val
25            cur = cur.next
26            i += 1
27        return res  
28
29
30# Your Solution object will be instantiated and called as such:
31# obj = Solution(head)
32# param_1 = obj.getRandom()