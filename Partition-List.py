1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
8        before_head = ListNode(0)
9        after_head = ListNode(0)
10        before = before_head
11        after = after_head
12        curr = head
13        while curr:
14            if curr.val < x:
15                before.next = curr
16                before = before.next
17            else:
18                after.next = curr
19                after = after.next
20            curr = curr.next
21        after.next = None
22        before.next = after_head.next
23        return before_head.next
24