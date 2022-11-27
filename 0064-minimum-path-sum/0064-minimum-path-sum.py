class Solution:
    def backtrack(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]
        
        if i < 0 or j < 0:
            return float('inf')
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        left = grid[i][j] + self.backtrack(i - 1, j, grid, dp)
        up = grid[i][j] + self.backtrack(i, j - 1, grid, dp)
        
        dp[i][j] = min(left, up)
        
        return min(left, up)        
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1] * len(grid[0]) for i in range(len(grid))]
        
        return self.backtrack(len(grid) - 1, len(grid[0]) - 1, grid, dp)