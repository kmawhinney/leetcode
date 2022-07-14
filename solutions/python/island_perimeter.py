class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            
            perimeter = 0
            
            visited.add((r, c))
            perimeter += dfs(r, c + 1) #right
            perimeter += dfs(r, c - 1) #left
            perimeter += dfs(r + 1, c) #up
            perimeter += dfs(r - 1, c) #down
            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
