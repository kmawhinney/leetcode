# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head

        while prev:
            curr = curr.next
            if curr == None or curr.val != prev.val:
                prev.next = curr
                prev = curr
        
        return head
