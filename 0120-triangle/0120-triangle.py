class Solution:
    def dfs(self, i, j, m, n, triangle, dp):
        if i == m - 1:
            return triangle[m - 1][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        down = triangle[i][j] + self.dfs(i + 1, j, m, n, triangle, dp)
        downRight = triangle[i][j] + self.dfs(i + 1, j + 1, m, n, triangle, dp)
        
        dp[i][j] = min(down, downRight)
        
        return min(down, downRight)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])
        
        dp = [[-1] * n for _ in range(m)]
        
        return self.dfs(0, 0, m, n, triangle, dp)