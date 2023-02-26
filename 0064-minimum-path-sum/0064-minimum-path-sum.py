class Solution:
    def dfs(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]
        
        if i < 0 or j < 0:
            return float('inf')
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = grid[i][j] + self.dfs(i - 1, j, grid, dp)
        left = grid[i][j] + self.dfs(i, j - 1, grid, dp)
        
        dp[i][j] = min(up, left)
        
        return min(up, left)
    
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[-1] * n for _ in range(m)]
        
        return self.dfs(m - 1, n - 1, grid, dp)