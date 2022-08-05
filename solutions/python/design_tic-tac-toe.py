from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.row_map = defaultdict(int)
        self.col_map = defaultdict(int)
        self.leftdiag_map = defaultdict(int)
        self.rightdiag_map = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        self.row_map[(player, row)] += 1
        self.col_map[(player, col)] += 1
        
        if col == row:
            self.leftdiag_map[player] += 1
        if col + row == self.size - 1:
            self.rightdiag_map[player] += 1
        
        if (self.size in self.row_map.values() or
            self.size in self.col_map.values() or
            self.size in self.leftdiag_map.values() or
            self.size in self.rightdiag_map.values()):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
