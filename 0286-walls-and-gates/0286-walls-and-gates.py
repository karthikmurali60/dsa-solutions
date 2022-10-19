class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        rows = len(rooms)
        cols = len(rooms[0])
        vis = [[0] * cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append([i, j, 0])
                    vis[i][j] = 1
        
        while queue:
            r, c, d = queue.pop(0)
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                
                if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1 or rooms[nr][nc] == -1 or rooms[nr][nc] == 0 or vis[nr][nc] == 1:
                    continue
                    
                vis[nr][nc] = 1
                rooms[nr][nc] = d + 1
                queue.append([nr, nc, d + 1])
                
                    
                