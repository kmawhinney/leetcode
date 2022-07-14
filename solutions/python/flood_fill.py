class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        rows, cols = len(image), len(image[0])
        starting_color = image[sr][sc]
        
        if starting_color == color:
            return image
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return
            
            if image[r][c] == starting_color:
                image[r][c] = color
                dfs(r + 1, c) #down
                dfs(r - 1, c) #up
                dfs(r, c + 1) #right
                dfs(r, c - 1) #left
            
        dfs(sr, sc)
        return image
