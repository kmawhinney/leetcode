from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        # Early exit if word length greater than cell count
        if rows * cols < len(word):
            return False
        
        # Early exit if letter occurance in word greater than on board
        word_letters = Counter(word)
        board_letters = []
        for r in range(rows):
            for c in range(cols):
                board_letters.append(board[r][c])
        board_letters = Counter(board_letters)
        for letter in word_letters:
            if word_letters[letter] > board_letters[letter]:
                return False

      
        # Suffix is what is left to match
        def backtrack(r, c, suffix):
            if len(suffix) == 0:
                return True

            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] != suffix[0]):
                return False

            # Temporarily mark current cell as visited
            board[r][c] = "#"            
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if backtrack(nr, nc, suffix[1:]):
                    return True

            # Reset cell to original value
            board[r][c] = suffix[0]


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, word):
                        return True
        return False
