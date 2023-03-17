class Solution:
    def dfs(self, i, j, index, m, n, word, board, vis):
        if index == len(word) - 1:
            return True
        
        
        if board[i][j] == word[index]:
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or vis[ni][nj] or board[ni][nj] != word[index + 1]:
                    continue
                    
                vis[i][j] = 1
                if self.dfs(ni, nj, index + 1, m, n, word, board, vis):
                    return True
                vis[i][j] = 0
                
        return False
                    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        vis = [[0] * n for _ in range(m)]
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, m, n, word, board, vis):
                        return True
                                
        return False