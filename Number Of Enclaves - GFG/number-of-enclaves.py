#User function Template for python3

from typing import List

class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        
        m, n = len(grid), len(grid[0])
        
        vis = [[0] * n for _ in range(m)]
        
        numCells = 0
        
        queue = []
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    vis[i][j] = 1
                    queue.append([i, j])
                    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            row, col = queue.pop(0)

            for di, dj in directions:
                ni, nj = row + di, col + dj

                if ni < 0 or ni >= m or nj < 0 or nj >= n or vis[ni][nj] or grid[ni][nj] == 0:
                    continue
                
                vis[ni][nj] = 1
                queue.append([ni, nj])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    numCells += 1
                    
        return numCells


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends