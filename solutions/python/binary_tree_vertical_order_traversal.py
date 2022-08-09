# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        position_map = defaultdict(list)
        visited = set()
        q = deque()
        
        q.append((root, 0))
        visited.add(root)
        
        while q:
            node, position = q.popleft()
            position_map[position].append(node.val)
            
            if node.left:
                q.append((node.left, position - 1))
                visited.add(node.left)
                
            if node.right:
                q.append((node.right, position + 1))
                visited.add(node.right)
            
        return [position_map[key] for key in sorted(position_map.keys())]
