class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '-1'
            
            if i >= 0 and i < len(grid) and j - 1 >= 0 and j < len(grid[0]) and grid[i][j-1] == '1':
                dfs(i, j - 1)
            if i >= 0 and i < len(grid) and j >= 0 and j + 1 < len(grid[0]) and grid[i][j+1] == '1':
                dfs(i, j + 1)
            if i - 1 >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i-1][j] == '1':
                dfs(i - 1, j)
            if i >= 0 and i + 1 < len(grid) and j >= 0 and j < len(grid[0]) and grid[i+1][j] == '1':
                dfs(i + 1, j)
        
        numberOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    numberOfIslands += 1
                    dfs(i, j)
        
        return numberOfIslands