class Solution:
    def dfs(self, i, j, end, m, n, maze, vis):
        if vis[i][j]:
            return False
        
        if [i, j] == end:
            return True
        
        vis[i][j] = 1
        
        right, left, down, up = j + 1, j - 1, i + 1, i - 1
        
        while right < n and maze[i][right] == 0:
            right += 1
            
        if self.dfs(i, right - 1, end, m, n, maze, vis):
            return True
        
        while left >= 0 and maze[i][left] == 0:
            left -= 1
                        
        if self.dfs(i, left + 1, end, m, n, maze, vis):
            return True
        
        while up >= 0 and maze[up][j] == 0:
            up -= 1
            
        if self.dfs(up + 1, j, end, m, n, maze, vis):
            return True
        
        while down < m and maze[down][j] == 0:
            down += 1
            
        if self.dfs(down - 1, j, end, m, n, maze, vis):
            return True
        
        return False
                
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        
        vis = [[0] * n for _ in range(m)]
        
        return self.dfs(start[0], start[1], destination, m, n, maze, vis)