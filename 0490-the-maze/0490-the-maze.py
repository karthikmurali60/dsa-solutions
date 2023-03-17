class Solution:
    def dfs(self, i, j, m, n, maze, dest, vis):
        if vis[i][j]:
            return False
        
        if [i, j] == dest:
            return True
        
        vis[i][j] = 1
        
        up, down, left, right = i - 1, i + 1, j - 1, j + 1
        
        while up >= 0 and maze[up][j] == 0:
            up -= 1
            
        if self.dfs(up + 1, j, m, n, maze, dest, vis):
            return True
        
        while down <= m - 1 and maze[down][j] == 0:
            down += 1
            
        if self.dfs(down - 1, j, m, n, maze, dest, vis):
            return True
        
        while left >= 0 and maze[i][left] == 0:
            left -= 1
            
        if self.dfs(i, left + 1, m, n, maze, dest, vis):
            return True
        
        while right <= n - 1 and maze[i][right] == 0:
            right += 1
            
        if self.dfs(i, right - 1, m, n, maze, dest, vis):
            return True
        
        return False
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        
        vis = [[0] * n for _ in range(m)]
        
        return self.dfs(start[0], start[1], m, n, maze, destination, vis)