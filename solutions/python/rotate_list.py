# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        new_tail = head
        for i in range(length-k % length-1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head
