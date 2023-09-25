# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid_node(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
        
            return (is_valid_node(node.left, left, node.val) and
                    is_valid_node(node.right, node.val, right))

        return is_valid_node(root, float("-inf"), float("inf"))
