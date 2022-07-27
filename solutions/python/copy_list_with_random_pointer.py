"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copymap = {None: None}
        
        # create copies without pointers
        curr = head
        while curr:
            copy = Node(curr.val)
            copymap[curr] = copy
            curr = curr.next
        
        # add in pointers to copied list
        curr = head
        while curr:
            copy = copymap[curr]
            copy.next = copymap[curr.next]
            copy.random = copymap[curr.random]
            curr = curr.next
        
        return copymap[head]
