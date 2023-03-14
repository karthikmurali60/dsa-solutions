class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        vis = [[-1] * n for _ in range(m)]
        
        queue = []
        
        minTime = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    vis[i][j] = 2
                    queue.append([i, j, 0])
                elif grid[i][j] == 1:
                    vis[i][j] == 1
                    
        while queue:
            row, col, time = queue.pop(0)
            
            minTime = max(minTime, time)
            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0 or grid[nr][nc] == 2 or vis[nr][nc] == 2:
                    continue
                    
                vis[nr][nc] = 2
                grid[nr][nc] = 2
                queue.append([nr, nc, time + 1])
                
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return minTime
