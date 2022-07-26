# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse list to go from end -> beginning
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        end = prev
        
        # remove nth node
        end_curr = end
        temp_n = n
        while temp_n > 1:
            end_curr = end_curr.next
            temp_n -= 1
        removed = end_curr
        
        # reverse list again from beginning -> end but skip removed
        prev, curr = None, end
        count = n
        while curr:
            if count == 1:
                curr = curr.next
                count -= 1
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1
        return prev
