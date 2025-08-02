# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast and fast.next: # Step 1: Find the middle
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr: # Step 2: Reverse second half
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        first = head
        second = prev
        while second: # Step 3: Compare first and second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
                
            
            
            