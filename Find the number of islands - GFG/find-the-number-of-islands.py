#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, i, j, grid, vis):
        if not vis[i][j] and grid[i][j] == 1:
            vis[i][j] = 1
            
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]) or vis[ni][nj] or (grid[ni][nj] == 0):
                    continue
                
                self.dfs(ni, nj, grid, vis)
        
    
    def numIslands(self,grid):
        #code here
        
        m, n = len(grid), len(grid[0])
        
        vis = [[0] * n for _ in range(m)]
        
        numIslands = 0
        
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    numIslands += 1
                    self.dfs(i, j, grid, vis)
                    
        return numIslands

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends