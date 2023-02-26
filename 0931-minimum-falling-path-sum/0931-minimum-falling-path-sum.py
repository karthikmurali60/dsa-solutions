class Solution:
    def dfs(self, i, j, m, n, matrix, dp):
        if j < 0 or j > n - 1:
            return float('inf')
        
        if i == m - 1:
            return matrix[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        dp[i][j] = matrix[i][j] + min(self.dfs(i + 1, j - 1, m, n, matrix, dp), self.dfs(i + 1, j, m, n, matrix, dp), self.dfs(i + 1, j + 1, m, n, matrix, dp))
        
        return dp[i][j]
    
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[-1] * n for _ in range(m)]
        
        minSum = float('inf')
        
        for j in range(n):
            minSum = min(minSum, self.dfs(0, j, m, n, matrix, dp))
            
        return minSum