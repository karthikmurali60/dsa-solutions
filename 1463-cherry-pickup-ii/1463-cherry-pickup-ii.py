class Solution:
    def dfs(self, i, j1, j2, m, n, grid, dp):
        if j1 < 0 or j1 > n - 1 or j2 < 0 or j2 > n - 1:
            return -float('inf')
        
        if i == m - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
            
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]
        
        maxSum = -float('inf')
        
        for dj1 in range(-1, 2):
            for dj2 in range(-1, 2):
                value = 0
                
                nj1 = j1 + dj1
                nj2 = j2 + dj2
                
                if j1 == j2:
                    value = grid[i][j1]
                else:
                    value = grid[i][j1] + grid[i][j2]
                
                value += self.dfs(i + 1, nj1, nj2, m, n, grid, dp)
                
                maxSum = max(maxSum, value)

        dp[i][j1][j2] = maxSum
        
        return maxSum

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[[-1] * n for _ in range(n)] for __ in range(m)]
        
        return self.dfs(0, 0, n - 1, m, n, grid, dp)