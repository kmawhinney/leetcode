class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        result = 0
        visited = set()

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r,c) in visited or
                board[r][c] == "."):
                return
            
            visited.add((r,c))
            
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X" and (r,c) not in visited:
                    dfs(r,c)
                    result += 1
        return result
