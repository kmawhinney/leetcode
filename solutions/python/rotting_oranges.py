from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        minutes = 0
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    fresh += 1
                if grid[r][c] == 2 and (r, c) not in visited:
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and ((nr, nc)) not in visited:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
            if q: # don't increment time if we've already rotted all oranges
                minutes += 1
        
        if fresh > 0:
            return -1
        else:
            return minutes
