class Solution:
    def dfs(self, i, j, m, n, board, vis):
        vis[i][j] = 1
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or vis[ni][nj] or board[ni][nj] == "X":
                continue
            
            board[ni][nj] = "J"
            self.dfs(ni, nj, m, n, board, vis)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        
        vis = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O" and not vis[i][j]:
                    board[i][j] = "J"
                    self.dfs(i, j, m, n, board, vis)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "J":
                    board[i][j] = "O"