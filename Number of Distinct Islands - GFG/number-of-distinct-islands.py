#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, i, j, grid, vis, path, bi, bj):
        vis[i][j] = 1
        
        path.append(tuple([i - bi, j - bj]))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]) or vis[ni][nj] or grid[ni][nj] == 0:
                continue
            
            self.dfs(ni, nj, grid, vis, path, bi, bj)

    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        
        s = set()
        
        m, n = len(grid), len(grid[0])
        
        vis = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    path = []
                    self.dfs(i, j, grid, vis, path, i, j)
                    s.add(tuple(path))
                    
        return len(s)

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
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends