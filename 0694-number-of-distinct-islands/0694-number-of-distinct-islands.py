class Solution:
    def dfs(self, i, j, bi, bj, m, n, grid, vis, path):
        vis[i][j] = 1
        
        path.append(tuple[i - bi, j - bj])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] == 0 or vis[ni][nj] == 1:
                continue
                
            self.dfs(ni, nj, bi, bj, m, n, grid, vis, path)    
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        
        vis = [[0] * n for _ in range(m)]
        
        s = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    path = []
                    
                    self.dfs(i, j, i, j, m, n, grid, vis, path)
                    
                    s.add(tuple(path))
                    
        return len(s)