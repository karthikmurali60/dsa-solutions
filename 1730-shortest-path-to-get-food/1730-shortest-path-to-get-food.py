class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        distance = 1000000000
        
        rows = len(grid)
        cols = len(grid[0])
        
        vis = [[0] * cols for i in range(rows)]
        queue = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    queue.append([i, j, 0])
                    vis[i][j] = 1
                    
        
        while queue:
            r, c, d = queue.pop(0)
            
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                
                if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1:
                    continue
                    
                if grid[nr][nc] == "X":
                    continue
                    
                if vis[nr][nc] == 1:
                    continue
                    
                queue.append([nr, nc, d + 1])
                if grid[nr][nc] == "#":
                    distance = min(distance, d + 1)
                vis[nr][nc] = 1
            
        if distance == 1000000000:
            return -1
        else:
            return distance
                    
                
            
            