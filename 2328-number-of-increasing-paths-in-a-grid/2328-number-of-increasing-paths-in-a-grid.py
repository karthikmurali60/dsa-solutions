class Solution:
    def dfs(self, i, j, m, n, matrix, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        
        answer = 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or matrix[ni][nj] <= matrix[i][j]:
                continue
            
            answer += self.dfs(ni, nj, m, n, matrix, dp)
            
        dp[i][j] = answer % 1000000007
        
        return dp[i][j]
    
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
                
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, m, n, grid, dp)
                
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
                
        return ans % 1000000007