# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       past = None
       future = None
       curr = head

       while curr:
        future = curr.next
        curr.next = past
        past = curr
        curr = future
       
       return past
