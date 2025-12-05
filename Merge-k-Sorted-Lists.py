1import heapq
2from typing import List, Optional
3
4class ListNode:
5    def __init__(self, val=1, next=None):
6        self.val = val
7        self.next = next
8
9class Solution:
10    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
11        heap = []
12        for idx, node in enumerate(lists):
13            if node:
14                heapq.heappush(heap, (node.val, idx, node))
15        dummy = ListNode(0)
16        curr = dummy
17        while heap:
18            val, idx, node = heapq.heappop(heap)
19            curr.next = node
20            curr = curr.next
21            if node.next:
22                heapq.heappush(heap, (node.next.val, idx, node.next))
23        return dummy.next