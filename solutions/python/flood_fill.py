# BFS Approach (preferred)
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = set()
        q = deque()
        start_color = image[sr][sc]
        
        q.append((sr, sc))
        visited.add((sr, sc))
        image[sr][sc] = color

        while q:
            r, c = q.popleft()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and image[nr][nc] == start_color and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    image[nr][nc] = color
        
        return image



# DFS Approach
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        rows, cols = len(image), len(image[0])
        starting_color = image[sr][sc]
        
        if starting_color == color:
            return image
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return
            
            if image[r][c] == starting_color:
                image[r][c] = color
                dfs(r + 1, c) #down
                dfs(r - 1, c) #up
                dfs(r, c + 1) #right
                dfs(r, c - 1) #left
            
        dfs(sr, sc)
        return image
