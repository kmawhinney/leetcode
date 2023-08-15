# BFS Approach (preferred)
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            area = 0
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                area += 1
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and ((nr, nc)) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        return max_area



# DFS Approach
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        visited = set()
        curr_area = 0
        max_area = 0
        
        
        def dfs(r, c):
            nonlocal curr_area
            
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            curr_area += 1
            
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if (nr in range(rows) and
                    nc in range(cols) and
                    (nr, nc) not in visited and
                    grid[nr][nc] == 1):
                    dfs(nr, nc)
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, curr_area)
                    curr_area = 0
        
        return max_area
