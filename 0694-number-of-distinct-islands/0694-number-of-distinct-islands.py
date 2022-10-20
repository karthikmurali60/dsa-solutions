class Solution:
    def dfs(self, i, j, rows, cols, grid, vis, island, br, bc):
        vis[i][j] = 1
        island.append(tuple([i - br, j - bc]))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for dr, dc in directions:
            nr, nc = dr + i, dc + j
            
            if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1 or vis[nr][nc] == 1 or grid[nr][nc] != 1:
                continue
            
            self.dfs(nr, nc, rows, cols, grid, vis, island, br, bc)
            
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        count = 0
        
        rows, cols = len(grid), len(grid[0])
        
        vis = [[0] * cols for i in range(rows)]
        distinctIslands = set()
        
        for i in range(rows):
            for j in range(cols):
                if vis[i][j] != 1 and grid[i][j] == 1:
                    island = []
                    
                    self.dfs(i, j, rows, cols, grid, vis, island, i, j)
                    
                    distinctIslands.add(tuple(island))
        
        return len(distinctIslands)
        