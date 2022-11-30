class Solution:
    def backtrack(self, i, j1, j2, rows, cols, grid, dp):
        if j1 < 0 or j2 < 0 or j1 >= cols or j2 >= cols:
            return -float('inf')

        if i == rows - 1:
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
                if j1 == j2:
                    value = grid[i][j1]
                else:
                    value = grid[i][j1] + grid[i][j2]

                value += self.backtrack(i + 1, j1 + dj1, j2 + dj2, rows, cols, grid, dp)

                maxSum = max(maxSum, value)

        dp[i][j1][j2] = maxSum
        
        return maxSum

    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[[-1]*cols for _ in range(cols)] for __ in range(rows)]
        
        return self.backtrack(0, 0, cols - 1, rows, cols, grid, dp)
