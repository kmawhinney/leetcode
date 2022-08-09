from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()
        steps = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    q.append((r, c))
                    visited.add((r, c))
                    break
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                if grid[r][c] == "#":
                    return steps
                
                directions = [[1, 0], # down
                              [-1, 0], # up
                              [0, 1], # right
                              [0, -1]] # left

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        (nr, nc) not in visited and
                        grid[nr][nc] != "X"):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            steps += 1
            
        return -1
