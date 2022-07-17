# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque() # takes in a node and a depth
        max_depth = 0
        result = 0
        depth_map = collections.defaultdict(list) # depth: [val]
        
        queue.append((root, 0))
        while queue:
            node, depth = queue.popleft()
            depth_map[depth].append(node.val)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
            if depth > max_depth:
                max_depth = depth
        
        result = sum(depth_map[max_depth])
        return result
