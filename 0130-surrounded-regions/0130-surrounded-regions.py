class Solution:
    def dfs(self, i, j, rows, cols, board, vis):
        vis[i][j] = 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for dr, dc in directions:
            nr, nc = dr + i, dc + j
            
            if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1 or vis[nr][nc] == 1 or board[nr][nc] == 'X':
                continue
            
            self.dfs(nr, nc, rows, cols, board, vis)
            
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        vis = [[0] * cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and board[i][j] == 'O':
                    self.dfs(i, j, rows, cols, board, vis)
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and vis[i][j] == 0:
                    board[i][j] = 'X'
                    
        return board