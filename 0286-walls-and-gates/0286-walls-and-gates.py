class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        queue = []
        
        m, n = len(rooms), len(rooms[0])
        
        vis = [[0] * n for _ in range(m)]
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i, j, 0])
                    vis[i][j] = 1
                    
        while len(queue) != 0:
            r, c, d = queue.pop(0)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nr > m - 1 or nc < 0 or nc > n - 1 or rooms[nr][nc] == -1 or rooms[nr][nc] == 0 or vis[nr][nc] == 1:
                    continue
                    
                vis[nr][nc] = 1
                rooms[nr][nc] = d + 1
                
                queue.append([nr, nc, d + 1])    
        