class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        ans = [[0] * cols for i in range(rows)]
        vis = [[0] * cols for i in range(rows)]
        
        queue = []
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append([i, j, 0])
                    ans[i][j] = 0
         
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue:
            r, c, d = queue.pop(0)

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                    
                if nr < 0 or nr > rows-1 or nc < 0 or nc > cols-1:
                    continue

                if vis[nr][nc] == 1:
                    continue
                
                if mat[nr][nc] == 0:
                    vis[nr][nc] = -1
                    continue

                vis[nr][nc] = 1
                queue.append([nr, nc, d + 1])
                ans[nr][nc] = d + 1
            
        return ans
                        
                