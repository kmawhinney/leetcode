from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = defaultdict(int) # (player, row):count
        self.cols = defaultdict(int) # (player, col):count
        self.diag = defaultdict(int) # player:count
        self.anti_diag = defaultdict(int)  # player:count

    def move(self, row: int, col: int, player: int) -> int:
        # Make move
        self.rows[(player, row)] += 1
        self.cols[(player, col)] += 1
        if row == col:
            self.diag[player] += 1
        if row + col == self.size - 1:
            self.anti_diag[player] += 1

        # Check if winner
        if (self.rows[(player, row)] == self.size or
            self.cols[(player, col)] == self.size or
            self.diag[player] == self.size or
            self.anti_diag[player] == self.size):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
