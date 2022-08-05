from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
            
        while q and fresh > 0:
            for i in range(len(q)): # go through each rotten orange, then increment time
                r, c = q.popleft()
                directions = [[1, 0], # down
                              [-1, 0], # up
                              [0, 1], # right
                              [0, -1]] # left

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            time += 1
            
        if fresh > 0:
            return -1
        else:
            return time
