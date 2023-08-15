"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone_map = {}

        def dfs(node):
            if node in clone_map:
                return clone_map[node]

            clone = Node(node.val)
            clone_map[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        
        if node:
            return dfs(node)
        else:
            return None
