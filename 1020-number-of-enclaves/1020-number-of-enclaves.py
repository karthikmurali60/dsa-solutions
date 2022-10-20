class Solution:
    def dfs(self, grid, i, j, rows, cols):
        grid[i][j] = 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dr, dc in directions:
            nr, nc = dr + i, dc + j
            
            if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1 or grid[nr][nc] != 1:
                continue

            self.dfs(grid, nr, nc, rows, cols)
                
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        
        rows, cols = len(grid), len(grid[0])
                
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == 1:
                    self.dfs(grid, i, j, rows, cols)
                   
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
                    
        return count
                    