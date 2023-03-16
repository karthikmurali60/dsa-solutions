class Solution:
    def dfs(self, i, j, m, n, matrix, dp):
        if dp[i][j] != 1:
            return dp[i][j]
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or matrix[ni][nj] <= matrix[i][j]:
                continue
            
            operation = 1 + self.dfs(ni, nj, m, n, matrix, dp)
            
            dp[i][j] = max(dp[i][j], operation)
        
        return dp[i][j]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[1] * n for _ in range(m)]
        
        ans = -1e9
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(i, j, m, n, matrix, dp))
                                
        return ans