# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs_inorder(node):
            if node:
                return dfs_inorder(node.left) + [node.val] + dfs_inorder(node.right)
            else:
                return []

        return dfs_inorder(root)[k-1]
