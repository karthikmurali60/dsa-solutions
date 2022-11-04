class Solution:
    def dfs(self, grid, visited, i, j, rows, cols):
        visited[i][j] = 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for dr, dc in directions:
            nr, nc = dr + i, dc + j
            
            if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1 or grid[nr][nc] == '0' or visited[nr][nc] == 1:
                continue
            
            self.dfs(grid, visited, nr, nc, rows, cols)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        numberOfIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    numberOfIslands += 1
                    self.dfs(grid, visited, i, j, rows, cols)
                    
        return numberOfIslands