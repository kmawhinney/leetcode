class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = collections.defaultdict(list)
        col_map = collections.defaultdict(list)
        box_map = collections.defaultdict(list)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in row_map[r] or
                    board[r][c] in col_map[c] or
                    board[r][c] in box_map[r // 3, c //3]):
                    return False
                else:
                    row_map[r].append(board[r][c])
                    col_map[c].append(board[r][c])
                    box_map[r // 3, c // 3].append(board[r][c])
        return True
