class Solution:
    def backtrack(self, i, j, triangle, dp):
        if i == len(triangle) - 1:
            return triangle[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        down = triangle[i][j] + self.backtrack(i + 1, j, triangle, dp)
        downLeft = triangle[i][j] + self.backtrack(i + 1, j + 1, triangle, dp)
        
        dp[i][j] = min(down, downLeft)
        
        return min(down, downLeft)
                
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[rows - 1])
        
        dp = [[-1] * cols for i in range(rows)]
        
        return self.backtrack(0, 0, triangle, dp)