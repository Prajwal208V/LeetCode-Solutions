1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next or k == 0:
9            return head
10
11        tail = head
12        n = 1
13        while tail.next:
14            tail = tail.next
15            n += 1
16
17        tail.next = head
18        k %= n
19        if k == 0:
20            tail.next = None
21            return head
22
23        steps = n - k - 1
24        new_tail = head
25        for _ in range(steps):
26            new_tail = new_tail.next
27
28        new_head = new_tail.next
29        new_tail.next = None
30        return new_head
31
32        