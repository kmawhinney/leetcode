# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse_list(head):
            curr, prev = head, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        first_half = head
        second_half = reverse_list(slow)       
        max_sum = 0
        
        while second_half:
            curr_sum = first_half.val + second_half.val
            max_sum = max(max_sum, curr_sum)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_sum
