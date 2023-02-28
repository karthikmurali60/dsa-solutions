#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)


class Solution:
    def dfs(self, i, j, bi, bj, m, n, grid, vis, islands):
        vis[i][j] = 1
        islands.append(tuple([i - bi, j - bj]))
        
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni > m - 1 or nj < 0 or nj > n - 1 or grid[ni][nj] == 0 or vis[ni][nj] == 1:
                continue
            
            self.dfs(ni, nj, bi, bj, m, n, grid, vis, islands)
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        
        s = set()
        
        m, n = len(grid), len(grid[0])
        
        vis = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    islands = []
                    
                    self.dfs(i, j, i, j, m, n, grid, vis, islands)
                    
                    s.add(tuple(islands))
                    
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