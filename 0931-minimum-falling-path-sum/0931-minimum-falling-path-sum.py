class Solution:
    def backtrack(self, i, j, matrix, dp, rows, cols):
        if j < 0 or j > cols - 1:
            return float('inf')
        
        if i == 0:
            return matrix[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        top = matrix[i][j] + self.backtrack(i - 1, j, matrix, dp, rows, cols)
        topLeft = matrix[i][j] + self.backtrack(i - 1, j - 1, matrix, dp, rows, cols)
        topRight = matrix[i][j] + self.backtrack(i - 1, j + 1, matrix, dp, rows, cols)
        
        dp[i][j] = min(top, topLeft, topRight)
        
        return min(top, topLeft, topRight)
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[-1] * cols for i in range(rows)]
        
        maxSum = float('inf')
        
        for j in range(cols):
            maxSum = min(maxSum, self.backtrack(rows - 1, j, matrix, dp, rows, cols))
            
        return maxSum