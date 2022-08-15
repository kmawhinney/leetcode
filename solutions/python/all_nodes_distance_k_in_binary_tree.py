# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def makeGraph(self, root):
        adj_list = defaultdict(list)
        queue = deque()
        queue.append(root)
        
        while queue:
            curr = queue.popleft()
            
            if curr.left:
                adj_list[curr].append(curr.left)
                adj_list[curr.left].append(curr)
                queue.append(curr.left)
            
            if curr.right:
                adj_list[curr].append(curr.right)
                adj_list[curr.right].append(curr)
                queue.append(curr.right)
                
        return adj_list
    
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        if k == 0:
            return [target.val]
        
        graph = self.makeGraph(root)
        queue = deque()
        visited = set()
        depth = 0
        result = []
        
        queue.append(target)
        
        while queue and depth <= k:
            for i in range(len(queue)):
                curr = queue.popleft()
                
                if curr not in visited:
                    for neighbour in graph[curr]:
                        queue.append(neighbour)
                        
                    if depth == k:
                        result.append(curr.val)
                        
                visited.add(curr)
            depth += 1
            
        return result
