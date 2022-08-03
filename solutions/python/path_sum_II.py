# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        def dfs(node, curr_sum, path):
            if not node:
                return False
            
            curr_sum += node.val
            curr_path = path + [node.val]
            
            if node.left:
                dfs(node.left, curr_sum, curr_path)
                
            if node.right:
                dfs(node.right, curr_sum, curr_path)                
            
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(curr_path)
            
        dfs(root, 0, [])
        
        return result
